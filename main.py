from extract import extractData
import numpy as np

def getDestList(paths, start, total_time = 0):
    destinations = []
    for i in range(len(paths)):
        if (paths[i][0] == start):
            destinations.append([
                paths[i][1],              # dest
                paths[i][2],              # travel_time
                total_time + paths[i][2], # total_time
                False                     # stop
                ])
#    print(destinations)
    return destinations

def bruteForce(paths, start, dest, total_time = 0, history = {}):
    print(history)
    print(start)
    if (start in history):
        print('looped')
        return []
    histories = []
    destinations = getDestList(paths, start, total_time)
    print(np.asarray(destinations))
    for each_dest in destinations:
        new_hist = history.copy()
        new_hist.update({start: total_time})
        print(new_hist)
        if (dest in new_hist):
            print('reached dest')
            return [new_hist]    
        histories += bruteForce(paths, each_dest[0], dest, each_dest[2], new_hist)
       
    return histories

paths_FloydWarshall_example = [
    # start, dest, travel_time
    [1, 2, 1],
    [1, 4, 4],
    [2, 1, 2],
    [2, 3, -2],
    [3, 1, 3],
    [4, 1, 4],
    [4, 2, -5],
    [4, 3, -1]
]

#print(*bruteForce(paths_FloydWarshall_example, 1, 3), sep='\n')

nodes, edges = extractData()
#print(edges)
print(*bruteForce(edges, 366428456, 366416066), sep='\n')