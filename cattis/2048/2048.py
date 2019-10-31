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

print(data)