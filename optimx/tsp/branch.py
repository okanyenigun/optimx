import numpy as np


class TSPSolverBranchAndBound:
    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix
        self.num_nodes = len(distance_matrix)
        self.best_path = None
        self.best_cost = np.inf

    def solve(self, start_node=None, cycle=True):
        """
        Solves the TSP using the branch-and-bound approach.

        Parameters:
            - start_node: The node to start from (default is 0).
            - cycle: Whether to return to the starting node at the end (True) or not (False).

        Returns:
            - best_path: List representing the optimal path taken.
            - best_cost: The minimum cost for this path.
        """
        # Set default start node to 0 if not provided
        if start_node is None:
            start_node = 0

        # Reset best path and cost for fresh solving
        self.best_path = None
        self.best_cost = np.inf

        # Initialize the stack with the root node
        stack = [(start_node, [start_node], {start_node}, 0)]
        
        while stack:
            current_node, path, visited, current_cost = stack.pop()
            
            # If all nodes have been visited, check if this path is the best
            if len(path) == self.num_nodes:
                if cycle:
                    # Complete the cycle by returning to the start node
                    current_cost += self.distance_matrix[path[-1]][start_node]
                if current_cost < self.best_cost:
                    self.best_path = path + ([start_node] if cycle else [])
                    self.best_cost = current_cost
            else:
                # Generate children nodes by considering all unvisited nodes
                unvisited = set(range(self.num_nodes)) - visited
                for next_node in unvisited:
                    new_path = path + [next_node]
                    new_cost = current_cost + self.distance_matrix[current_node][next_node]
                    
                    # Prune paths that exceed the current best cost
                    if new_cost < self.best_cost:
                        stack.append((next_node, new_path, visited | {next_node}, new_cost))
        
        return self.best_path
