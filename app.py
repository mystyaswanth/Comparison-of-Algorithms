from flask import Flask, render_template, request, redirect, url_for
import csv
import logging
from algorithms.greedy import greedy_knapsack, greedy_tsp
from algorithms.dynamic import dp_knapsack, dp_tsp
from algorithms.backtracking import bt_knapsack, bt_tsp
from algorithms.branch_bound import bb_knapsack, bb_tsp
from algorithms.divide_conquer import dc_knapsack, dc_tsp
from utils import measure_time

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

def load_knapsack_data(filename):
    items = []
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 3:
                    try:
                        value = int(row[0])
                        weight = int(row[1])
                        name = row[2]
                        items.append((value, weight, name))
                    except ValueError:
                        logging.warning(f"Invalid data in {filename}: {row}")
                        continue
    except FileNotFoundError:
        logging.info(f"{filename} not found, using defaults")
    except Exception as e:
        logging.error(f"Error loading {filename}: {e}")
    return items

def load_tsp_data(filename):
    cities = []
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2:
                    try:
                        x = float(row[0])
                        y = float(row[1])
                        cities.append((x, y))
                    except ValueError:
                        logging.warning(f"Invalid data in {filename}: {row}")
                        continue
    except FileNotFoundError:
        logging.info(f"{filename} not found, using defaults")
    except Exception as e:
        logging.error(f"Error loading {filename}: {e}")
    return cities

default_knapsack = [
    (60, 10, 'A'),
    (100, 20, 'B'),
    (120, 30, 'C')
]
default_capacity = 50

default_tsp = [(0, 0), (2, 3), (5, 2), (6, 6), (8, 3)]

algorithms = [
    ('Greedy', greedy_knapsack, greedy_tsp),
    ('Dynamic Programming', dp_knapsack, dp_tsp),
    ('Backtracking', bt_knapsack, bt_tsp),
    ('Branch & Bound', bb_knapsack, bb_tsp),
    ('Divide & Conquer', dc_knapsack, dc_tsp)
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run():
    knapsack_items = load_knapsack_data('datasets/knapsack.csv')
    if not knapsack_items:
        knapsack_items = default_knapsack
    capacity = default_capacity
    tsp_cities = load_tsp_data('datasets/tsp.csv')
    if not tsp_cities:
        tsp_cities = default_tsp

    results = []

    for name, knap_func, _ in algorithms:
        try:
            solution, t = measure_time(knap_func, knapsack_items, capacity)
            selected, value = solution
            results.append([name, 'Knapsack', str(selected), f"{t:.6f}", value])
        except Exception as e:
            logging.error(f"Error in {name} Knapsack: {e}")
            results.append([name, 'Knapsack', 'Error', 'N/A', 'N/A'])

    for name, _, tsp_func in algorithms:
        try:
            solution, t = measure_time(tsp_func, tsp_cities)
            tour, dist = solution
            results.append([name, 'TSP', str(tour), f"{t:.6f}", dist])
        except Exception as e:
            logging.error(f"Error in {name} TSP: {e}")
            results.append([name, 'TSP', 'Error', 'N/A', 'N/A'])

    # Save results to CSV
    with open('results/output.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Algorithm', 'Problem', 'Solution', 'Time', 'Metric'])
        writer.writerows(results)

    return redirect(url_for('results'))

@app.route('/results')
def results():
    results_data = []
    try:
        with open('results/output.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            results_data = list(reader)
    except FileNotFoundError:
        logging.info("No results file found")
    except Exception as e:
        logging.error(f"Error reading results: {e}")
    return render_template('results.html', results=results_data)

if __name__ == '__main__':
    app.run(debug=True)
