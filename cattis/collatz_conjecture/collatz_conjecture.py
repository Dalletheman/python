import sys
import math

# True if submitting to kattis
# fast method
input = True

def readdata(input):
    if input:
        data = sys.stdin.read().splitlines()
    else:
        with open('sample.in') as f:
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

def loop(input):
    data = list_2_matrix(readdata(input))
    count = 0
    while not(data[count][0] == 0 and data[count][1] == 0):
        a = data[count][0]
        b = data[count][1]
        calc_collatz_2(a, b)
        count += 1
    return 0
# recursive not working
def calc_collatz(a, s_a, b, s_b):
    if a % 2 == 0:
        a_prim = int(a / 2)
    else:
        a_prim = 3 * a + 1
    if b % 2 == 0:
        b_prim = int(b / 2)
    else:
        b_prim = 3 * b + 1

    if a == b:
        return [a, s_a, s_b]
    elif a == 1:
        x = calc_collatz(a, s_a, b_prim, s_b + 1)
        return x
    elif b == 1:
        y = calc_collatz(a_prim, s_a + 1, b, s_b)
        return y
    else:
        x = calc_collatz(a, s_a, b_prim, s_b + 1)
        y = calc_collatz(a_prim, s_a + 1, b, s_b)

        x_sum = x[1] + x[2]
        y_sum = y[1] + y[2]

        if x_sum > y_sum:
            return x
        else:
            return y

def calc_first_collatz(n, dict):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = n * 3 + 1
        count += 1
        dict[n] = count
def calc_second_collatz(n, dict):
    count = 0
    if n in dict:
        return count, n
    else:
        while n > 1:
            if n % 2 == 0:
                n = int(n / 2)
            else:
                n = n * 3 + 1
            count += 1
            if n in dict:
                return count, n
def calc_collatz_2(a,b):

    dict = {a : 0}
    calc_first_collatz(a, dict)
    res = calc_second_collatz(b, dict)
    count = res[0]
    n = res[1]
    print(str(a) + " needs " + str(dict[n]) + " steps, " + str(b) + " needs " + str(count) + " steps, they meet at " + str(n))


loop(input)
