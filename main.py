from extract import extractData
import time
from load_map import loadMap
<<<<<<< HEAD
import time
from load_map import loadMap
import random
#import numpy as np

def getDestList(paths, start, total_length = 0):
    destinations = []
    for i in range(len(paths)):
        if (paths[i]['s_node_id'] == start):
            destinations.append({
                'e_node_id': paths[i]['e_node_id'], 
                'length': paths[i]['length'], 
                'total_length': total_length + paths[i]['length'],
                'stop': False 
                })
#    print(destinations)
    return destinations

def bruteForce(paths, start, end, total_length = 0, history = {}):
    #print(history)
    #print(start)
    if (start in history):
        print('looped')
        return []
    histories = []
    destinations = getDestList(paths, start, total_length)
    #print(np.asarray(destinations))
    for each_dest in destinations:
        new_hist = history.copy()
        new_hist.update({start: total_length})
        if (end in new_hist):
            print('reached dest')
            return [new_hist]    
        histories += bruteForce(paths, each_dest['e_node_id'], end, each_dest['total_length'], new_hist)
        
    return histories
=======
import random
#import numpy as np
from algorithms import bruteForce, dijkstra, bellman_ford

def benchmark(algo_func, paths, start, end):
    start_time = time.time()
    result = algo_func(paths, start, end)
    end_time = time.time()
    return result, (end_time-start_time)
>>>>>>> 93a87c9ffe7fe2f7c1f9e3626cb7f0c209d82702

def benchmark(algo_func, paths, start, end):
    start_time = time.time()
    result = algo_func(paths, start, end)
    end_time = time.time()
    return result, (end_time-start_time)

paths_FloydWarshall_example = [
<<<<<<< HEAD
    {'s_node_id': 1, 'e_node_id': 2, 'length': 1},
    {'s_node_id': 1, 'e_node_id': 4, 'length': 4},
    {'s_node_id': 2, 'e_node_id': 1, 'length': 2},
    {'s_node_id': 2, 'e_node_id': 3, 'length': -2},
    {'s_node_id': 3, 'e_node_id': 1, 'length': 3},
    {'s_node_id': 4, 'e_node_id': 1, 'length': 4},
    {'s_node_id': 4, 'e_node_id': 2, 'length': -5},
    {'s_node_id': 4, 'e_node_id': 3, 'length': -1}
=======
    {'start': 1, 'dest': 2, 'travel_time': 1},
    {'start': 1, 'dest': 4, 'travel_time': 4},
    {'start': 2, 'dest': 1, 'travel_time': 2},
    {'start': 2, 'dest': 3, 'travel_time': -2},
    {'start': 3, 'dest': 1, 'travel_time': 3},
    {'start': 4, 'dest': 1, 'travel_time': 4},
    {'start': 4, 'dest': 2, 'travel_time': -5},
    {'start': 4, 'dest': 3, 'travel_time': -1}
>>>>>>> 93a87c9ffe7fe2f7c1f9e3626cb7f0c209d82702
]

#print(*bruteForce(paths_FloydWarshall_example, 1, 3), sep='\n')

<<<<<<< HEAD
def bruteforce():
    nodes, edges = extractData()
    #print(edges)
    found_paths, run_time = benchmark(bruteForce, edges, 4639027499, 366430703)
    print('==============================================')
    print('Found paths:')
    print(*found_paths, sep='\n')
    print('\nTime elapsed:')
    print(run_time)
    return

if __name__ == "__main__":
    bruteforce()
=======
>>>>>>> 93a87c9ffe7fe2f7c1f9e3626cb7f0c209d82702
def edgeConverter(edges_format_1):
    #for i in edges_format_1:
    #    print(i)
    #    print(edges_format_1[i])
    
    edges_format_2 = [{'start': i[0], 'dest': i[1], 'travel_time': edges_format_1[i]['length']} for i in edges_format_1]
    return edges_format_2

<<<<<<< HEAD
def runAlgorithm(algorithm, graph):
=======
def runAlgorithm(algorithm, map_name):
    # load the graph from map file
    graph = loadMap(map_name)
    
>>>>>>> 93a87c9ffe7fe2f7c1f9e3626cb7f0c209d82702
    # pick start and end point randomly (seeded)
    random.seed(10)
    start, end = random.sample(sorted(graph._node), 2)
    print('start: ', start)
    print('end: ', end)
    
    # convert edge to our format
    edges_format_ours = edgeConverter(graph.edges)
    found_paths, run_time = benchmark(algorithm, edges_format_ours, start, end)
    print('==============================================')
    print('Found paths:')
    print(*found_paths, sep='\n')
    print('\nTime elapsed:')
    print(run_time)
    '''
    nodes, edges = extractData()
    #print(edges)
    found_paths, run_time = benchmark(bruteForce, edges, 4639027499, 366430703)
    print('==============================================')
    print('Found paths:')
    print(*found_paths, sep='\n')
    print('\nTime elapsed:')
    print(run_time)
    '''
    return

if __name__ == "__main__":
<<<<<<< HEAD
    map_name = 'newgraph_conso.osm'
    # load the graph from map file
    graph = loadMap(map_name)
    
    runAlgorithm(bruteForce, graph)
    
    
=======
    runAlgorithm(bruteForce, 'newgraph_conso.osm')
>>>>>>> 93a87c9ffe7fe2f7c1f9e3626cb7f0c209d82702
