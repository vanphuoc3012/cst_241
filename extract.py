# Python program to convert JSON to Python
import os

def getDir(file_name):
    full_path = os.path.realpath(__file__)
    path, filename = os.path.split(full_path)
    dir = os.path.join(path, file_name)
    print(dir)
    return dir

def extractData(txt, prefix):
    data = []
    for line in txt:
        line_data = line.split()
        #print(line_data)
        if line_data[0] == prefix:
            data.append([int(i) for i in line_data[1:]])
    return data

def saveToTxt(data, name):
    dir = getDir(name)
    with open(dir, 'w', encoding='utf8') as f:
        for line in data:
            #print(line)
            f.write(line)
    return

def extract_c_d_t():
    dir_coords = getDir('coords_NYC.txt')
    dir_distance = getDir('distance_NYC.txt')
    dir_time = getDir('time_NYC.txt')

    txt_coords = open(dir_coords, encoding='utf8')
    txt_distance = open(dir_distance, encoding='utf8')
    txt_time = open(dir_time, encoding='utf8')

    coords = extractData(txt_coords, 'v')
    distance = extractData(txt_distance, 'a')
    time = extractData(txt_time, 'a')

    #print(coords)
    #print(distance)
    #print(time)
    return coords, distance, time
