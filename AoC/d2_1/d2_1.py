import sys

def read():

    read_data = []
    for i in sys.stdin:
        x = i
        read_data.append(x)

    return read_data
def raw_read():
    g = input()
    return g

def string_2_int(data):

    int_data = data.split(',')

    int_data = list(map(int,int_data))

    return int_data

def calc(data,n,v):

    run = True
    index = 0
    data[1] = n
    data[2] = v
    while run:
        op_code = data[index]
        if op_code == 99:
            run = False
        elif op_code == 1:
            input_1 = data[data[index + 1]]
            input_2 = data[data[index + 2]]
            pos = data[index + 3]
            data[pos] = input_1 + input_2
        elif op_code == 2:
            input_1 = data[data[index + 1]]
            input_2 = data[data[index + 2]]
            pos = data[index + 3]
            data[pos] = input_1 * input_2
        else:
            run = False

        index += 4

    return data[0]


def main():
    data = raw_read()
    int_data = string_2_int(data)


    goal = 19690720

    for n in range(0,100):
        for v in range(0,100):
            result = calc(int_data.copy(),n,v)
            if result == goal:
                print("Noun is: " + str(n) )
                print("Verb is: " + str(v) )
                print("Answer is: " + str(100*n + v))

    x_0 = calc(int_data,80,51)
    print(x_0)





main()