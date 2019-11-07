import sys
import math

# True if submitting to kattis
# Recursion
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

def check(data,sum):
    n = data[0][0]
    width = math.pow(2,-3/4)
    height = math.pow(2,-5/4)
    def check_inside(j):

        p1 = False
        p2 = False
        if data[1][j] > 0:
            data[1][j] = data[1][j] - 1
            p1 = True
        else:
            if j < n - 2:
                p1 = check_inside(j + 1)
        if data[1][j] > 0:
            data[1][j] = data[1][j] - 1
            p2 = True
        else:
            if j < n - 2:
                p2 = check_inside(j + 1)
        if p1 and p2:
            if (j)%2 == 0:
                    sum[0] = sum[0] + width/(math.pow(2,j/2))
            else:
                    sum[0] = sum[0] + height/(math.pow(2,(j-1)/2))
        return p1 and p2
    return check_inside(0)


data = readdata(input)
data = list_2_matrix(data)
sum = [0]

if check(data,sum):
    print(sum[0])
else:
    print('impossible')

