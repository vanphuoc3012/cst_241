import networkx as nx
from collections import deque

def find_maximum_flow_using_edmonds_karp(graph, source, sink):
    """
    Finds the maximum flow in a graph from a source node to a sink node using the Edmonds-Karp algorithm.
    
    Args:
        graph (networkx.DiGraph): A directed graph with capacity attributes on edges.
        source (int): The source node.
        sink (int): The sink node.
    
    Returns:
        flow_value: The maximum flow from the source to the sink.
        flow_dict: A dictionary containing edges and their respective flow values.
    """
    residual_graph = graph.copy()
    
    flow_dict = {(u, v): 0 for (u, v) in graph.edges()}
    
    def bfs(residual_graph, source, sink):
        """Find an augmenting path using BFS."""
        visited = {source: None}
        queue = deque([source])
        
        while queue:
            u = queue.popleft()
            if u == sink:
                break
                
            for v in residual_graph.neighbors(u):
                if v not in visited and residual_graph[u][v]['capacity'] > 0:
                    visited[v] = u
                    queue.append(v)
        
        if sink not in visited:
            return None
        
        path = []
        current = sink
        while current is not None:
            path.append(current)
            current = visited[current]
        path.reverse()
        return path
    
    max_flow = 0
    
    while True:
        path = bfs(residual_graph, source, sink)
        if path is None:
            break
            
        min_capacity = float('inf')
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            min_capacity = min(min_capacity, residual_graph[u][v]['capacity'])
        
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            
            residual_graph[u][v]['capacity'] -= min_capacity
            if (u, v) in flow_dict:
                flow_dict[(u, v)] += min_capacity
            
            if not residual_graph.has_edge(v, u):
                residual_graph.add_edge(v, u, capacity=0)
            residual_graph[v][u]['capacity'] += min_capacity
            
        max_flow += min_capacity
    
    return max_flow, flow_dict