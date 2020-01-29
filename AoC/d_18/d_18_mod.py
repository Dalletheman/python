import math
import copy


keys = "abcdefghijklmnopqrstuvwxyz"

def read():
    with open('input_2.txt') as f:
        data = f.read().splitlines()
    return data


def print_map(data):
    height = len(data)
    width = len(data[0])

    for i in range(0, height):
        for j in range(0, width):
            print(data[i][j], end='')
        print('')

def get_pos(data, char):
    length = len(data)
    for i in range(0, length):
        if char in data[i]:
            x = data[i].index(char)
            y = i
            break
    return [x,y]


def get_routes(source, data):
    xs, ys = source
    visited = []
    queue = [(xs, ys, 0, "")]
    routes = {}
    for (x, y, dist, route) in queue:
        item = data[y][x]
        if item not in ".#@" and dist > 0:

            if not item.isupper():
                routes[item] = (dist, route)
            route = route + item

        for pos in [(0, -1),(1, 0),(0, 1),(-1, 0)]:
            next_x = x + pos[0]
            next_y = y + pos[1]
            if data[next_y][next_x] not in '#' and (next_x,next_y) not in visited:
                queue.append((next_x, next_y, dist + 1, route))
        visited.append((x,y))
    return routes



def find_routes(data):
    routes = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            item = data[i][j]
            if item in keys + "@":
                routes[item] = get_routes((j, i), data)
    return routes


def find_shortest_path(routes):
    keys = []
    queue =


def main():
    data = read()
    print_map(data)
    routes = find_routes(data)
    find_shortest_path(routes)





main()

