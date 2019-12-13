import sys


def read():
    g = input()
    return g

def split(data):

    int_data = data.split(',')
    print(int_data)


    return int_data

def cordinates(data):
    x = 0
    y = 0
    cord = [[0,0]]
    for i in range(0,len(data)):
        change = delta(data[i])

        x += change[0]
        y += change[1]

        cord.append([x,y])
    return cord

def delta(move):
    delta = int(move[1:])
    y_delta = 0
    x_delta = 0
    if move[0] == 'U':
        y_delta = delta
    elif move[0] == 'D':
        y_delta = delta * -1
    elif move[0] == 'L':
        x_delta = delta * -1
    elif move[0] == 'R':
        x_delta = delta
    return x_delta, y_delta

def check_intersection(a_cord, b_cord):

    manh_length = 1000000

    x_final = 0
    y_final = 0
    for i in range(0,len(a_cord) - 1):
        x_a_min = min(a_cord[i][0], a_cord[i + 1][0])
        x_a_max = max(a_cord[i][0], a_cord[i + 1][0])
        y_a_min = min(a_cord[i][1], a_cord[i + 1][1])
        y_a_max = max(a_cord[i][1], a_cord[i + 1][1])

        for j in range(0, len(b_cord) - 1):
            x_b_min = min(b_cord[j][0], b_cord[j + 1][0])
            x_b_max = max(b_cord[j][0], b_cord[j + 1][0])
            y_b_min = min(b_cord[j][1], b_cord[j + 1][1])
            y_b_max = max(b_cord[j][1], b_cord[j + 1][1])

            if x_a_min == x_a_max and y_b_min == y_b_max:
                if x_b_min < x_a_min and x_b_max > x_a_min and y_a_min < y_b_min and y_a_max > y_b_min:
                    x_cross = x_a_min
                    y_cross = y_b_min
                    manh_temp = abs(x_cross) + abs(y_cross)
                    if manh_temp < manh_length:
                        manh_length = manh_temp
                        x_final = x_cross
                        y_final = y_cross
            if y_a_min == y_a_max and x_b_min == x_b_max:
                if x_a_min < x_b_min and x_a_max > x_b_min and y_b_min < y_a_min and y_b_max > y_a_min:
                    x_cross = x_b_min
                    y_cross = y_a_min
                    manh_temp = abs(x_cross) + abs(y_cross)
                    if manh_temp < manh_length:
                        manh_length = manh_temp
                        x_final = x_cross
                        y_final = y_cross

    print("x:" + str(x_final))
    print("y:" + str(y_final))

    return manh_length

def main():
    print("Enter first cable")
    a = split(read())
    a_cord = cordinates(a.copy())
    print(a_cord)
    print("Enter seconds cable")
    b = split(read())
    b_cord = cordinates(b.copy())
    print(check_intersection(a_cord,b_cord))


main()