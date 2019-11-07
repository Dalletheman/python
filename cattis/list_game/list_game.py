import sys
import math

# True if submitting to kattis
input = True

def readdata(input):
    if input:
        data = sys.stdin.read().splitlines()
    else:
        with open('listgame.01.in') as f:
            data = f.read().splitlines()
    return data

def calc_int(number):
    rest = number
    i = 1
    count = 0
    run = True
    while run:
        if rest % (i + 1) == 0:
            count += 1
            rest = rest / (i + 1)
            if rest == 1:
                run = False
        elif (i + 1) > math.sqrt(rest):
            count += 1
            run = False
        else:
            i += 1
    return count

data = int(readdata(input)[0])
n = calc_int(data)
print(n)
