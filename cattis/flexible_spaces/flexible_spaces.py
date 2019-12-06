import sys
import math

# True if submitting to kattis

input = True

def readdata(input):
    if input:
        data = sys.stdin.read().splitlines()
    else:
        with open('B.in') as f:
            data = f.read().splitlines()
    return data
def list_2_matrix(str_list):
    matrix = []
    length = len(str_list)
    for i in range(0, length):
        temp = str_list[i].split(' ')
        temp = list(map(int, temp))
        matrix.append(temp)
    return matrix

def spaces(data):
    length = data[0][0]
    spaces = data[0][1]
    a = data[1][:]
    a.insert(0,0)
    a.append(length)

    space =[]

    for i in range(0, spaces + 1):
        for j in range(0, spaces - i + 1):
            diff = a[j + 1 + i] - a[j]
            if not(diff in space):
                space.append(diff)

    space.sort()
    return space

data = readdata(input)
data = list_2_matrix(data)


sort_space = spaces(data)

for i in range(0, len(sort_space)):
    print(sort_space[i], end=' ')


