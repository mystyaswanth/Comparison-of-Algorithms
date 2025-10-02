Algorithm Comparison Tool
=========================
This is a Flask web application that compares various optimization algorithms for solving the 0/1 Knapsack Problem and the Traveling Salesman Problem (TSP). It implements Greedy, Dynamic Programming, Backtracking, Branch & Bound, and Divide & Conquer approaches, measuring their execution times and displaying results.

What does this application do?
-------------------------------
- Loads problem data from CSV files (knapsack.csv for items: value,weight,name; tsp.csv for cities: x,y).
- Runs all algorithms on the data and compares solutions and performance.
- Displays results in a web interface with tables showing algorithm, problem, solution, time, and metric (value/distance).
- Saves results to output.csv for further analysis.


# How to run?
You can run the application in one of the following ways:

1. Press `F5`. This will start the application in debug mode.

2. Open a terminal by going to 'View' -> 'Terminal'. Then, run following command:
   > `flask --app app.py run --host=0.0.0.0 --port=5000 --debug`

This will start the application in development mode.

## Algorithms Implemented
- **Greedy**: Fast heuristics (fractional knapsack for value/weight; nearest neighbor for TSP).
- **Dynamic Programming**: Optimal solutions (DP table for Knapsack; Held-Karp for TSP).
- **Backtracking**: Exhaustive search (combinations for Knapsack; permutations for TSP).
- **Branch & Bound**: Pruned search with bounds (sorted items for Knapsack; state-based for TSP).
- **Divide & Conquer**: Recursive splitting (recursive Knapsack; insertion heuristic for TSP).

## Data Formats
- Knapsack: CSV with columns value,weight,name (e.g., 60,10,A).
- TSP: CSV with columns x,y (e.g., 0,0).

## Testing
Run `python app.py` and visit http://localhost:5000 to run comparisons.

Via curl command:
-----------------
1. Open a terminal.
2. Type the following command:
   > `curl http://localhost:5000`
3. Press 'Enter' to make the request.

Via Thunder Client:
-------------------
1. Click on the Thunder Client icon on the activity bar on the side. If you can't find it, you can search for 'Thunder Client' in the 'View' -> 'Extensions' menu.
2. Once Thunder Client is open, click on 'New Request'.
3. In the 'Request URL' field, enter the URL of your application (e.g., http://localhost:5000) and select the HTTP method from the dropdown menu.
5. Click on 'Send' to make the request.

Visit [Flask Quickstart](https://flask.palletsprojects.com/en/latest/quickstart/) for more information.

