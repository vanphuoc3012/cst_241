import networkx as nx
import osmnx as ox
from pyrosm.data import sources, get_data
from pyrosm import OSM
import matplotlib.pyplot as plt
%matplotlib inline

vn = get_data("vietnam")

raw_data_osm = OSM('raw.pbf')

nodes, edges = raw_data_osm.get_network(nodes=True, network_type='driving')

# print(nodes)
# print(edges)

ox.settings.use_cache = True

# download street network data from OSM and construct a MultiDiGraph model
G = ox.graph_from_bbox(bbox=(10.81864,10.78786,106.71535,106.64738), network_type='all_public', retain_all=True)
G = raw_data_osm.to_graph(nodes=nodes, edges=edges, graph_type='networkx', retain_all=True)

# calculate maximum vehicle between edges base on edges properties


# impute edge (driving) speeds and calculate edge travel times
# G = ox.routing.add_edge_speeds(G)
# G = ox.routing.add_edge_travel_times(G)

# # you can convert MultiDiGraph to/from GeoPandas GeoDataFrames
# gdf_nodes, gdf_edges = ox.convert.graph_to_gdfs(G)

# print(gdf_nodes)

# G = ox.convert.graph_from_gdfs(gdf_nodes, gdf_edges, graph_attrs=G.graph)

# convert MultiDiGraph to DiGraph to use nx.betweenness_centrality functions
# choose between parallel edges by minimizing travel_time attribute value
# D = ox.convert.to_digraph(G, weight="travel_time")


# save graph as a geopackage or graphml file
# ox.io.save_graph_geopackage(G, filepath="./graph.gpkg")
# ox.io.save_graphml(G, filepath="./graph.graphml")

# ox.plot.plot_graph(G, save=True, show=True, filepath='./graph.png')
nx.draw(G, with_labels=True)
plt.savefig('graph.png', dpi=300, bbox_inches='tight')
plt.show()