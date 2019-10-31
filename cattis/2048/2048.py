import sys
input = False

# 0 = left; 1 = up; 2 = right; 3 = down

def readdata(input):
    if input:
        data = sys.stdin.read().splitlines()
    else:
        with open('1.in') as f:
            data = f.read().splitlines()
    return data

def list_2_matrix(str_list):
    matrix = []
    for i in range(0, length - 1):
        temp = str_list[i].split(' ')
        temp = list(map(int, temp))
        matrix.append(temp)
    return matrix

data = readdata(input)
length = len(data)
dir = int(data[length - 1])
matrix = list_2_matrix(data)
print(matrix)
for i in range(0,4):
    for j in range(1, 4):
        status = True
        action_index = -1
        index = j - 1
        if matrix[i][j] != 0:

            while status:

                if matrix[i][index + 1] == matrix[i][index]:
                    matrix[i][index] = matrix[i][index]*2
                    matrix[i][index + 1] = 0
                    action_index = index
                    status = False
                elif matrix[i][index] == 0:
                    matrix[i][index] = matrix[i][index + 1]
                    matrix[i][index + 1] = 0
                else:
                    status = False

                index -= 1
                if index == action_index:
                    status = False


print(matrix)
