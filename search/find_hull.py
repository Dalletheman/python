from matplotlib import pyplot as plt
import numpy as np
import time
import random

import sys
import math

# True if submitting to kattis
# fast method


def create_data():
    n = random.randint(50, 60)

    matrix = np.array([50,50])
    for i in range(0, n):
        x = random.randint(0,100)
        y = random.randint(0,100)
        matrix = np.vstack((matrix,[x,y]))

    return matrix

def readdata():
    with open('sample.in') as f:
        data = f.read().splitlines()
    return data
def list_2_matrix(str_list):

    length = len(str_list)
    for i in range(0, length):
        if i == 0:
            temp = str_list[i].split(' ')
            temp = list(map(int, temp))
            matrix = np.array([temp])
        else:
            temp = str_list[i].split(' ')
            temp = list(map(int, temp))
            matrix = np.vstack((matrix, temp))
    return matrix

def calc_hull(data):

    start_index = data.argmin(axis=0)[0]
    cordinates = np.array([data[start_index]])

    green = [0, 0.5 , 0.5]
    grey = [0 , 0 , 0, 0.5]
    dark_grey = [0, 0, 0, 0.7]
    blue = [65/255, 105/255, 225/255]
    red = [178/255, 34/255, 24/255]

    run = True
    count = 0

    while run:
        if count == 0:
            index = start_index
            prev_index = start_index
            prev_vec = np.array([data[index][0] - data[index][0],data[index][1]- data[index][1] - 1])

        max_angle = 0
        plt.ion()
        for i in range(0,len(data)):
            if not(index == i or prev_index == i):
                #plt.clf()
                plt.clf()
                plt.plot(data[0:len(data), 0], data[0:len(data), 1], color = dark_grey, marker = 'o', linestyle = 'None')
                plt.plot(data[index][0], data[index][1], 'ro', ms = 7)
                plt.plot(data[i][0], data[i][1], color = dark_grey, marker = 'o', ms = 10)
                plt.plot([data[index][0],data[i][0]],[data[index][1],data[i][1]],color = grey)
                if len(cordinates) == 2:
                    plt.plot([cordinates[0][0], cordinates[1][0]],[cordinates[0][1],cordinates[1][1]], color = green)
                elif len(cordinates) > 2:
                    for j in range(0, len(cordinates) - 1):

                        plt.plot([cordinates[j][0], cordinates[j + 1][0]], [cordinates[j][1], cordinates[j + 1][1]],color = green)
                vec = np.array([data[i][0] - data[index][0],data[i][1]-data[index][1]])
                prev_len = np.linalg.norm(prev_vec)
                vec_len = np.linalg.norm(vec)
                angle = math.acos((np.dot(vec,prev_vec))/(prev_len*vec_len))
                angle_cos = (np.dot(vec,prev_vec))/(prev_len*vec_len)
                if angle > max_angle:
                    max_angle = angle
                    best_index = i

                plt.plot([data[best_index][0], data[index][0]],[data[best_index][1], data[index][1]], color = blue)

                plt.draw()
                plt.pause(0.005)



        prev_vec = np.array([data[index][0] - data[best_index][0], data[index][1] - data[best_index][1]])
        prev_index = index
        index = best_index
        if index == start_index:
            run = False

        count += 1
        cordinates = np.vstack((cordinates, data[index]))




    plt.pause(10)
    return 0
#data = readdata()

#data = list_2_matrix(data)
data = create_data()
calc_hull(data)


x = data[0:9,0]
y = data[0:9,1]


plt.plot(x,y,'bo')
plt.show()






