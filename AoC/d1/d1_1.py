import sys

def read():

    read_data = []
    for i in sys.stdin:
        x = int(i)
        read_data.append(x)

    return read_data
def main():
    data = read()
    print(calc(data))

def calc(data):
    length = len(data)

    sum = 0
    for i in range(0,length):
        run = True
        temp = data[i]
        while run:
            temp = temp // 3
            temp -= 2;
            if temp <= 0:
                run = False
            else:
                sum += temp
    return sum
main()