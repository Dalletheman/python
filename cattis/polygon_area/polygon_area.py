import sys

# True if submitting to kattis
input = True

# 0 = left; 1 = up; 2 = right; 3 = down

def readdata(input):
    if input:
        data = sys.stdin.read().splitlines()
    else:
        with open('polygonarea_sample.in') as f:
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

data = readdata(input)
data = list_2_matrix(data)

n = data[0][0]

count = 1
while n != 0:
    pos_sum = 0
    neg_sum = 0
    for i in range(count, count + n - 1):
        pos_sum = pos_sum + data[i][0]*data[i + 1][1]
        neg_sum = neg_sum + data[i][1]*data[i + 1][0]
    pos_sum = pos_sum + data[count][1]*data[count + n - 1][0]
    neg_sum = neg_sum + data[count][0]*data[count + n - 1][1]

    area = (pos_sum-neg_sum)/2
    if area > 0:
        print('CCW',end=' ')

    else:
        print('CW', end=' ')
    print(abs(area))
    count = count + n + 1
    n = data[count - 1][0]







