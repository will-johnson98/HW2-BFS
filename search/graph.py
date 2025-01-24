import networkx as nx
from collections import deque

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        Performs BFS traversal and optional pathfinding.
        
        Args:
            start: Starting node
            end: Optional end node for pathfinding
            
        Returns:
            - List of nodes in BFS traversal order if end==None
            - Shortest path from start to end if path exists
            - None if end specified but no path exists
        """
        if start not in self.graph:
            return None
            
        queue = deque([(start, [start])])
        visited = {start}
        traversal = [start]

        while queue:
            vertex, path = queue.popleft()
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    traversal.append(neighbor)
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path))
                    
                    if neighbor == end:
                        return new_path
                        
        return traversal if end is None else None
