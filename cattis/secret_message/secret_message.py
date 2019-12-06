import sys
import math

# True if submitting to kattis

input = True

def readdata(input):
    if input:
        data = sys.stdin.read().splitlines()
    else:
        with open('secret.in') as f:
            data = f.read().splitlines()
    return data

def secret_mes(input):
    data = readdata(input)

    n = int(data[0])

    for i in range(0,n):
        length = len(data[i + 1])
        root = int(math.sqrt(length))

        if math.pow(root,2) != length:
            add = int(math.pow(root + 1, 2) - length)
            for j in range(0,add):
                data[i + 1] = data[i + 1] + '*'

        l = len(data[i + 1])
        l_root = int(math.sqrt(l))


        for ii in range(l - l_root, l):
            for jj in range(0, l_root):
                if data[i + 1][ii - l_root*jj] != '*':
                    print(data[i + 1][ii - l_root*jj], end='')
        print('')





secret_mes(input)