import sys
input = False

def readdata(input):
    if input:
        data = sys.stdin.read().splitlines()
    else:
        with open('1.in') as f:
            data = f.read().splitlines()
    return data

data = readdata(input)
length = len(data)


matrix = []

for i in range(0,length - 1):
    temp = data[i].split(' ')
    temp = list(map(int,temp))
    matrix.append(temp)

print(matrix)
