import networkx as nx
from networkx import Graph
import osmnx as ox
from osmnx import convert
from pyrosm.data import sources, get_data
from pyrosm import OSM
import matplotlib.pyplot as plt
from edmonds_karp import find_maximum_flow_using_edmonds_karp
# %matplotlib inline

ox.settings.use_cache = True

raw_data_osm = OSM('raw.pbf')
G = ox.graph_from_bbox(bbox=(10.81864,10.78786,106.71535,106.64738), network_type='drive', retain_all=True)
# G = raw_data_osm.to_graph(nodes=nodes, edges=edges, graph_type='networkx', retain_all=True, network_type='driving')

# Get largest strongly connected component
G = ox.truncate.largest_component(G, strongly=False)

# G = ox.simplification.simplify_graph(G)

G = ox.routing.add_edge_speeds(G)
G: Graph = ox.routing.add_edge_travel_times(G)

capacity_rules = {
        'motorway': 2000,
        'trunk': 1800,
        'primary': 1600,
        'secondary': 1200,
        'tertiary': 800,
        'residential': 400,
        'unclassified': 300,
        'service': 200
    }

for u, v, data in G.edges(data=True,  keys=True):
    highway_type = data.get('highway', 'unclassified')

    if isinstance(highway_type, list):
            highway_type = highway_type[0]

    base_capacity = capacity_rules.get(highway_type, 300)
    lanes = data.get('lanes', 1)
    if isinstance(lanes, list):
        lanes = float(lanes[0])
    else:
         lanes = float(lanes)
         
    speed = data.get('speed_kph', 30)
    travel_time = data.get('travel_time', 0)
    speed_factor = min(2.0, max(0.5, speed / 50))
    final_capacity = base_capacity * lanes * speed_factor
    data['capacity'] = final_capacity


for u, v, data in G.edges(data=True):
    print(f'u: {u}')
    print(f'v: {v}')
    print(f'capacity: {G[u, v]["capcity"]}')
    # print(f'data: {data}')

emonds_karp_maximum_flow, emonds_karp_flow_dict = find_maximum_flow_using_edmonds_karp(G, 366367322, 10910534491)

print(f'Emond Karps max value: {emonds_karp_maximum_flow}') 
print(f'Path: {emonds_karp_flow_dict}')

max_value, flow_dict = nx.maximum_flow(G, 366367322, 10910534491,  capacity='capacity')

print(f'Expected max value: {max_value}')
for flow in flow_dict:
    print(f'flow: {flow}, val: {flow_dict[flow]}')

ox.plot.plot_graph(nx.MultiDiGraph(G), save=True, show=True, filepath='./graph.png', node_size=1)
ox.plot.plot_graph_route(nx.MultiDiGraph(G), route=list(flow_dict.keys()))