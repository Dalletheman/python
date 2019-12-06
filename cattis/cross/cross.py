import sys
import math
from copy import copy, deepcopy

# True if submitting to kattis
# fast method
input = False

def readdata(input):
    if input:
        data = sys.stdin.read().splitlines()
    else:
        with open('cross.1.in') as f:
            data = f.read().splitlines()
    return data

def to_list(data):

    matrix = []
    for i in range(0,9):
        temp = [char for char in data[i]]
        matrix.append(temp)
    return matrix
def sudoku(data):
    #print_board(data)
    if valid_board(data.copy()):
        run = True
        master_count = 0
        while run:
            count = 0

            for n in range(1,10):
                # temp contains the crossed out board and a action flag [board, action_flag]

                temp = cross_out(deepcopy(data), str(n))
                if temp[1]:
                    pos = check_pos(temp[0])
                    if len(pos) > 0:
                        data = set_number(data, pos, n)
                        count += 1
                        master_count += 1
                        #print_board(data)
                        #print('')
            if count == 0:
                run = False
        if master_count > 0:
            print_board(data)
            #print("Finished with filling sudoku board")
        else:
            print('ERROR')
    else:
        print('ERROR')



def cross_out(data, n):

    action = False
    for i in range(0,9):
        if n in data[i]:
            action = True
            j = data[i].index(n)
            for count in range(0,9):
                data[i][count] = '-'
                data[count][j] = '-'

            ii_start = i//3 * 3
            jj_start = j//3 * 3


            for ii in range(ii_start, ii_start + 3):
                for jj in range(jj_start, jj_start + 3):
                    data[ii][jj] = '-'


    return data, action




def check_pos(data):

    points =[]
    for i in range(0,3):
        for j in range(0,3):
            count = 0
            pos = []
            ii_low = i * 3
            jj_low = j * 3
            for ii in range(ii_low, ii_low + 3):
                for jj in range(jj_low, jj_low + 3):
                    if data[ii][jj] == '.':
                        pos.append([ii,jj])
                        count += 1
            if count == 1:
                points.append(pos[0])

    return points

def set_number(data,pos, n):
    length = len(pos)
    for i in range(0, length):
        data[pos[i][0]][pos[i][1]] = str(n)

    return data

def print_board(data):
    #print('' + '\n' + "Board updated" + '\n')
    for i in range(0,9):
        #if i == 3 or i == 6:
        #    print("————————————————————")
        for j in range(0,9):
            print(data[i][j], end='')
            #if j == 2 or j == 5:
            #    print('|', end='')
        print('')

def valid_board(data):
    for n in range(1,10):
        if not(check_rows(data, str(n)) and check_cols(data, str(n)) and check_box(data, str(n))):
            return False
    return True

def check_rows(data, n):
    for i in range(0,9):
        if data[i].count(n) > 1:
            return False
    return True


def check_cols(data, n):
    test = 0
    for j in range(0, 9):
        c = [row[j] for row in data]
        if c.count(n) > 1:
            return False
    return True




def check_box(data, n):
    for i in range(0,3):
        for j in range(0,3):
            count = 0
            for k in range(0, 3):
                n_row = data[i*3 + k][(j*3) : (j*3 + 3)].count(n)
                count += n_row
            if count > 1:
                return False
    return True




string_data = readdata(input)
list_data = to_list(string_data)

sudoku(list_data)
