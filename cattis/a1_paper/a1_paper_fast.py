import sys
import math

# True if submitting to kattis
# fast method
input = True

def readdata(input):
    if input:
        data = sys.stdin.read().splitlines()
    else:
        with open('2.in') as f:
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

# calculate tape length and output if possible to build A1 paper
def calc_tape(data):
    n = data[0][0]
    i = 0
    run = True
    rest_area = 1
    tape_length = 0
    width = math.pow(2, -3 / 4)
    height = math.pow(2, -5 / 4)
    while run:

        n_paper = data[1][i]
        paper_area = 1/((math.pow(2,i + 1)))
        papers_needed = rest_area / paper_area

        if i % 2 == 0:
            paper_width = width/(math.pow(2,(i)/2))
            tape_length = tape_length + paper_width*papers_needed/2
        else:
            paper_height = height/(math.pow(2,(i - 1)/2))
            tape_length = tape_length + paper_height*papers_needed/2

        rest_area = rest_area - n_paper*paper_area
        i += 1

        if i + 1 >= n and rest_area > 0:
            run = False
            print('impossible')
        if rest_area <= 0:
            run = False
            print(tape_length)



data = readdata(input)
data = list_2_matrix(data)

calc_tape(data)