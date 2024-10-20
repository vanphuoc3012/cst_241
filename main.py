from extract import extract_c_d_t

def getDestList(paths, start, total_time = 0):
    destinations = []
    for i in range(len(paths)):
        if (paths[i]['start'] == start):
            destinations.append({
                'dest': paths[i]['dest'], 
                'travel_time': paths[i]['travel_time'], 
                'total_time': total_time + paths[i]['travel_time'],
                'stop': False 
                })
#    print(destinations)
    return destinations

def bruteForce(paths, start, dest, total_time = 0, history = {}):
#    print(history)
#    print(start)
    if (start in history):
#        print('looped')
        return []
    histories = []
    destinations = getDestList(paths, start, total_time)
#    print(np.asarray(destinations))
    for each_dest in destinations:
        new_hist = history.copy()
        new_hist.update({start: total_time})
        if (dest in new_hist):
#            print('reached dest')
            return [new_hist]    
        histories += bruteForce(paths, each_dest['dest'], dest, each_dest['total_time'], new_hist)
        
    return histories

paths_FloydWarshall_example = [
    {'start': 1, 'dest': 2, 'travel_time': 1},
    {'start': 1, 'dest': 4, 'travel_time': 4},
    {'start': 2, 'dest': 1, 'travel_time': 2},
    {'start': 2, 'dest': 3, 'travel_time': -2},
    {'start': 3, 'dest': 1, 'travel_time': 3},
    {'start': 4, 'dest': 1, 'travel_time': 4},
    {'start': 4, 'dest': 2, 'travel_time': -5},
    {'start': 4, 'dest': 3, 'travel_time': -1}
]

#print(*bruteForce(paths_FloydWarshall_example, 1, 3), sep='\n')
print(*bruteForce(paths_FloydWarshall_example, 1, 3), sep='\n')

coords, distance, time = extract_c_d_t()
