import sys

# True if submitting to kattis
input = True

# 0 = left; 1 = up; 2 = right; 3 = down

def readdata(input):
    if input:
        data = sys.stdin.read().splitlines()
    else:
        with open('6.in') as f:
            data = f.read().splitlines()
    return data

def list_2_matrix(str_list):
    matrix = []
    for i in range(0, length - 1):
        temp = str_list[i].split(' ')
        temp = list(map(int, temp))
        matrix.append(temp)
    return matrix

def shift_matrix(matrix, dir):
    x_shift = False
    y_shift = False
    shift_dir = 0
    range_min = 0
    range_max = 0
    if dir == 0:
        x_shift = True
        shift_dir = -1
        range_min = 1
        range_max = 4
    elif dir == 1:
        y_shift = True
        shift_dir = -1
        range_min = 1
        range_max = 4
    elif dir == 2:
        x_shift = True
        shift_dir = 1
        range_min = 2
        range_max = -1
    elif dir == 3:
        y_shift = True
        shift_dir = 1
        range_min = 2
        range_max = -1

    if x_shift:
        for i in range(0, 4):
            action_index = range_min + shift_dir*2
            for j in range(range_min, range_max, shift_dir*-1):
                status = True
                index = j + shift_dir
                if matrix[i][j] != 0:

                    while status:

                        if matrix[i][index - shift_dir] == matrix[i][index]:
                            matrix[i][index] = matrix[i][index] * 2
                            matrix[i][index - shift_dir] = 0
                            action_index = index
                            status = False
                        elif matrix[i][index] == 0:
                            matrix[i][index] = matrix[i][index - shift_dir]
                            matrix[i][index - shift_dir] = 0
                        else:
                            status = False

                        index = index + shift_dir
                        if index == action_index:
                            status = False
    elif y_shift:
        for j in range(0, 4):
            action_index = range_min + shift_dir * 2
            for i in range(range_min,range_max,shift_dir*-1):
                status = True
                index = i + shift_dir
                if matrix[i][j] != 0:
                    while status:
                        if matrix[index - shift_dir][j] == matrix[index][j]:
                            matrix[index][j] = matrix[index][j] * 2
                            matrix[index - shift_dir][j] = 0
                            action_index = index
                            status = False
                        elif matrix[index][j] == 0:
                            matrix[index][j] = matrix[index - shift_dir][j]
                            matrix[index - shift_dir][j] = 0
                        else:
                            status = False
                        index = index + shift_dir
                        if index == action_index:
                            status = False
    return matrix

def print_matrix(matrix):
    width = len(matrix[0])
    height = len(matrix)

    for i in range(0,height):
        for j in range(0,width):
            print(matrix[i][j], end= ' ')
        print('')


data = readdata(input)

length = len(data)
dir = int(data[length - 1])
matrix = list_2_matrix(data)


matrix = shift_matrix(matrix,dir)
print_matrix(matrix)
