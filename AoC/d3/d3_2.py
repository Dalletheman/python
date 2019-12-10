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

def check_intersection(a_cord, b_cord, a_move, b_move):

    cable_length = 1000000
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

                    temp_length = calc_cable_length(a_move, b_move, i, j)

                    x_temp_length = abs(b_cord[j][0] - x_cross)
                    y_temp_length = abs(a_cord[i][1] - y_cross)

                    tot_length = temp_length + x_temp_length + y_temp_length
                    if tot_length < cable_length:
                        cable_length = tot_length

            if y_a_min == y_a_max and x_b_min == x_b_max:
                if x_a_min < x_b_min and x_a_max > x_b_min and y_b_min < y_a_min and y_b_max > y_a_min:
                    x_cross = x_b_min
                    y_cross = y_a_min

                    temp_length = calc_cable_length(a_move, b_move, i, j)

                    x_temp_length = abs(a_cord[i][0] - x_cross)
                    y_temp_length = abs(b_cord[j][1] - y_cross)

                    tot_length = temp_length + x_temp_length + y_temp_length
                    if tot_length < cable_length:
                        cable_length = tot_length


    return cable_length

# returns length of cable just before crossing
def calc_cable_length(a_move, b_move, a_count, b_count):


    a_length = 0
    b_length = 0
    if a_count > 0:
        for i in range(0,a_count):
            a_sub_length = int(a_move[i][1:])
            a_length += a_sub_length
    if b_count > 0:
        for j in range(0,b_count):
            b_sub_length = int(b_move[j][1:])
            b_length += b_sub_length


    return a_length + b_length
def main():
    print("Enter first cable")
    a = split(read())
    a_cord = cordinates(a.copy())
    print(a_cord)
    print("Enter seconds cable")
    b = split(read())
    b_cord = cordinates(b.copy())
    print(check_intersection(a_cord,b_cord,a.copy(),b.copy()))


main()