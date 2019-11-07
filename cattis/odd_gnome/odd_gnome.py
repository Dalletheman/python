import sys


# True if submitting to kattis
input = True

def readdata(input):
    if input:
        data = sys.stdin.read().splitlines()
    else:
        with open('sample01.in') as f:
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

def calc_pos(n,data):

    for i in range(1,n + 1):
        n_gnome = data[i][0]

        pos = 0
        run = True
        j = 1
        while run:
            if data[i][j] + 1 != data[i][j + 1]:
                pos = j + 1
                run = False

            j += 1
            if j == n_gnome:
                run = False
        print(pos)

data = readdata(input)
data = list_2_matrix(data)
n = data[0][0]
calc_pos(n,data)