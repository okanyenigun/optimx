# optimx

**optimx** is a Python package designed to solve classic optimization problems. Its purpose is to provide efficient, flexible, and extendable solutions for a variety of optimization challenges.

Currently, **optimx** offers partial support for solving the Traveling Salesman Problem (TSP) through multiple algorithmic approaches, including brute force, dynamic programming, nearest neighbor, and branch-and-bound. This package aims to serve as a robust foundation for tackling optimization problems, with plans for additional algorithms and broader optimization support in future releases.

# Installation

You can install **optimx** via pip:

```bash
pip install optimx
```

# Tutorial

Here is a quick example to get started with **optimx** and see how it can be used to solve the Traveling Salesman Problem (TSP) with different algorithms.

```python
import optimx as ox

# Define a distance matrix representing the distances between nodes
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Set algorithm options and parameters
algorithm = "branch_and_bound"  # Options: "nearest_neighbor", "branch_and_bound", "genetic_algorithm"
node_names = None  # Optionally, specify node names, e.g., ["A", "B", "C", "D"]
start_node = None  # Optionally, specify a start node, e.g., "A"
cycle = False      # Set to True if the route should return to the start node
node_coordinates = None  # Optionally, specify coordinates, e.g., [(0, 0), (0, 1), (1, 0), (1, 1)]

# Solve the TSP using the specified algorithm and options
best_route = ox.solve_tsp(
    distance_matrix=distance_matrix,
    algorithm=algorithm,
    node_names=node_names,
    start_node=start_node,
    cycle=cycle
)

print("Best route:", best_route)
```

```python
Best route: [0, 1, 3, 2]
Total distance: 65
```

```python
total_distance = ox.calculate_tsp_distance_by_route(distance_matrix=distance_matrix, route=best_route, node_names=node_names)
print("Total distance:", total_distance)
```

```python
Total distance: 65
```

```python
ox.plot_tsp_route(best_route, node_names, node_coordinates, start_node, cycle)
```

## License

OptimX is licensed under the MIT License. See [LICENSE](Licence.md) for more details.

## Contributing

We welcome contributions to OptimX! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Contact

For any questions or feedback, please contact the author:

- **Okan Yenigün** - [okanyenigun@gmail.com](mailto:okanyenigun@gmail.com)
