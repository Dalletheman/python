import sys
import math

# True if submitting to kattis

input = True

def readdata(input):
    if input:
        data = sys.stdin.read().splitlines()
    else:
        with open('sample.in') as f:
            data = f.read().splitlines()
    return data


def crypt(input):
    data = readdata(input)

    count = 0

    while data[count] != '0':

        length = len(data[count + 1])
        key = data[count].split()
        key.pop(0)
        key_length = len(key)

        # number of whitespace that should pad the message
        ws_add = length % key_length
        if ws_add > 0:
            ws_add = key_length - ws_add
            for i in range(0, ws_add):
                data[count + 1] = data[count + 1] + ' '

        # number of iterations
        n = int(len(data[count + 1])/key_length)

        new_string = "'"
        for i in range(0,n):
            for j in range(0,key_length):
                index = int(key[j]) - 1
                temp = data[count + 1][i*key_length + index]
                new_string = new_string + data[count + 1][i*key_length + index]
        new_string = new_string + "'"
        count += 2
        print(new_string)

crypt(input)