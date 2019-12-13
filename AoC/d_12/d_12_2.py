from copy import copy, deepcopy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
def readdata():
    with open('input1.txt') as f:
        data = f.read().splitlines()
    return data

def calc_vel(pos, vel):


    for i in range(0, 3):

        for j in range(i + 1, 4):
            x1 = pos[i][0]
            y1 = pos[i][1]
            z1 = pos[i][2]
            x2 = pos[j][0]
            y2 = pos[j][1]
            z2 = pos[j][2]

            if x1 < x2:
                vel[i][0] += 1
                vel[j][0] -= 1
            elif x2 < x1:
                vel[i][0] -= 1
                vel[j][0] += 1
            if y1 < y2:
                vel[i][1] += 1
                vel[j][1] -= 1
            elif y2 < y1:
                vel[i][1] -= 1
                vel[j][1] += 1
            if z1 < z2:
                vel[i][2] += 1
                vel[j][2] -= 1
            elif z2 < z1:
                vel[i][2] -= 1
                vel[j][2] += 1
    return vel
def calc_pos(pos, vel):

    for i in range(0,len(pos)):
        pos[i][0] += vel[i][0]
        pos[i][1] += vel[i][1]
        pos[i][2] += vel[i][2]

    return pos

def calc_power(pos, vel):
    power = 0

    for i in range(0,len(pos)):
        pot = abs(pos[i][0]) + abs(pos[i][1]) + abs(pos[i][2])
        kin = abs(vel[i][0]) + abs(vel[i][1]) + abs(vel[i][2])

        power += (pot*kin)

    return power

def print_vel_diff(vel, prev_vel):

    for i in range(0, len(vel)):
        x_diff = vel[i][0] - prev_vel[i][0]
        y_diff = vel[i][1] - prev_vel[i][1]
        z_diff = vel[i][2] - prev_vel[i][2]

        vel_diff = [x_diff, y_diff, z_diff]

        print(vel_diff)
    print()


def calc_lcm(period):
    x1 = period[0]
    x2 = period[1]
    x3 = period[2]

    prime = [2,3,5,7,11,13,17,19]

    run = True
    while run:
        if x1 %


def main():
    data = readdata()
    print(data)
    pos = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
    vel = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    pos_init = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]

    period = []
    for n in range(0,3):
        pos = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
        vel = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

        run = True
        count = 0
        while run:
            vel = calc_vel(pos, vel)
            pos = calc_pos(pos, vel)
            if pos[0][n] == pos_init[0][n] and pos[1][n] == pos_init[1][n] and pos[2][n] == pos_init[2][n] and pos[3][n] == pos_init[3][n]:
                period.append(count + 2)
                run = False
            count += 1

    print(period)
    calc_lcm(period)




main()
