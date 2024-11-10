from osmnx.plot import plot_graph_route, plot_graph_routes
import networkx as nx


def plot_routes(graph, routes, **kwargs):
    if len(routes) == 1:
        return plot_graph_route(graph, routes[0], **kwargs)
    
    

    return plot_graph_routes(graph, routes, **kwargs)