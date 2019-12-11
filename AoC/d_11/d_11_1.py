from matplotlib.pyplot import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import matplotlib
import numpy as np
def read():
    val = input()
    str_list = val.split(',')
    int_list = list(map(int,str_list))
    return int_list

def run_operations(int_list, in_index, in_relative_base, in_memory, in_data):

    memory = in_memory
    total_length = len(int_list)
    index = in_index
    relative_base = in_relative_base
    run = True
    main_run = True

    # this is the output from the program
    output_arr = []
    while run:
        opcode = str(int_list[index])
        opcode_length = len(opcode)
        opcode_type = int(opcode[opcode_length - 1])



        mode_a = 0
        mode_b = 0
        mode_c = 0

        if opcode_length == 5:
            mode_a = int(opcode[0])
            mode_b = int(opcode[1])
            mode_c = int(opcode[2])
        elif opcode_length == 4:
            mode_b = int(opcode[0])
            mode_c = int(opcode[1])
        elif opcode_length == 3:
            mode_c = int(opcode[0])

        if opcode == "99":
            run = False
            main_run = False
        # 3,4,9 has one param
        elif opcode_type == 3:
            input_val = in_data
            input_param = int_list[index + 1]
            if mode_c == 0:
                if input_param >= total_length:
                    input_param = input_param - total_length
                    memory[input_param] = input_val
                else:
                    int_list[input_param] = input_val
            elif mode_c == 2:
                input_param = input_param + relative_base
                if input_param >= total_length:
                    input_param = input_param - total_length
                    memory[input_param] = input_val
                else:
                    int_list[input_param] = input_val
            index += 2

        elif opcode_type == 4:
            output_param = int_list[index + 1]
            output = 0
            if mode_c == 0:
                if output_param >= total_length:
                    output_param = output_param - total_length
                    if memory.get(output_param) == None:
                        output = 0
                    else:
                        output = memory.get(output_param)
                else:
                    output = int_list[output_param]
            elif mode_c == 1:
                output = output_param
            elif mode_c == 2:
                output_param = output_param + relative_base
                if output_param >= total_length:
                    output_param = output_param - total_length
                    if memory.get(output_param) == None:
                        output = 0
                    else:
                        output = memory.get(output_param)
                else:
                    output = int_list[output_param]

            output_arr.append(output)

            index += 2
            if len(output_arr) == 2:
                run = False
        else:

            param1 = int_list[index + 1]
            param2 = 0
            param3 = 0
            if mode_c == 0:
                if param1 >= total_length:
                    param1 = param1 - total_length
                    if memory.get(param1) == None:
                        param1 = 0
                    else:
                        param1 = memory.get(param1)
                else:
                    param1 = int_list[param1]
            elif mode_c == 2:
                param1 = param1 + relative_base
                if param1 >= total_length:
                    param1 = param1 - total_length
                    if memory.get(param1) == None:
                        param1 = 0
                    else:
                        param1 = memory.get(param1)
                else:
                    param1 = int_list[param1]

            if opcode_type != 9:

                if mode_b == 0:
                    param2_index = int_list[index + 2]
                    if param2_index >= total_length:
                        param2_index = param2_index - total_length
                        if memory.get(param2_index) == None:
                            param2 = 0
                        else:
                            param2 = memory.get(param2_index)
                    else:
                        param2 = int_list[param2_index]
                elif mode_b == 1:
                    param2 = int_list[index + 2]
                elif mode_b == 2:
                    param2_index = int_list[index + 2] + relative_base
                    if param2_index >= total_length:
                        param2_index = param2_index - total_length
                        if memory.get(param2_index) == None:
                            param2 = 0
                        else:
                            param2 = memory.get(param2_index)
                    else:
                        param2 = int_list[param2_index]

            if opcode_type == 1:
                sum = param1 + param2
                if mode_a == 0:
                    param3 = int_list[index + 3]
                    if param3 >= total_length:
                        new_index = param3 - total_length
                        memory[new_index] = sum
                    else:
                        int_list[param3] = sum
                elif mode_a == 2:
                    param3 = int_list[index + 3] + relative_base
                    if param3 >= total_length:
                        new_index = param3 - total_length
                        memory[new_index] = sum
                    else:
                        int_list[param3] = sum
                index += 4

            elif opcode_type == 2:
                sum = param1 * param2
                if mode_a == 0:
                    param3 = int_list[index + 3]
                    if param3 >= total_length:
                        new_index = param3 - total_length
                        memory[new_index] = sum
                    else:
                        int_list[param3] = sum
                elif mode_a == 2:
                    param3 = int_list[index + 3] + relative_base
                    if param3 >= total_length:
                        new_index = param3 - total_length
                        memory[new_index] = sum
                    else:
                        int_list[param3] = sum
                index += 4

            elif opcode_type == 5:

                if param1 != 0:
                    index = param2
                else:
                    index += 3

            elif opcode_type == 6:
                if param1 == 0:
                    index = param2
                else:
                    index += 3

            elif opcode_type == 7:

                if mode_a == 0:
                    param3 = int_list[index + 3]
                    if param1 < param2:
                        if param3 >= total_length:
                            new_index = param3 - total_length
                            memory[new_index] = 1
                        else:
                            int_list[param3] = 1
                    else:
                        if param3 >= total_length:
                            new_index = param3 - total_length
                            memory[new_index] = 0
                        else:
                            int_list[param3] = 0
                elif mode_a == 2:
                    param3 = int_list[index + 3] + relative_base
                    if param1 < param2:
                        if param3 >= total_length:
                            new_index = param3 - total_length
                            memory[new_index] = 1
                        else:
                            int_list[param3] = 1
                    else:
                        if param3 >= total_length:
                            new_index = param3 - total_length
                            memory[new_index] = 0
                        else:
                            int_list[param3] = 0

                index += 4

            elif opcode_type == 8:

                if mode_a == 0:
                    param3 = int_list[index + 3]
                    if param1 == param2:
                        if param3 >= total_length:
                            new_index = param3 - total_length
                            memory[new_index] = 1
                        else:
                            int_list[param3] = 1
                    else:
                        if param3 >= total_length:
                            new_index = param3 - total_length
                            memory[new_index] = 0
                        else:
                            int_list[param3] = 0
                elif mode_a == 2:
                    param3 = int_list[index + 3] + relative_base
                    if param1 == param2:
                        if param3 >= total_length:
                            new_index = param3 - total_length
                            memory[new_index] = 1
                        else:
                            int_list[param3] = 1
                    else:
                        if param3 >= total_length:
                            new_index = param3 - total_length
                            memory[new_index] = 0
                        else:
                            int_list[param3] = 0
                index += 4

            elif opcode_type == 9:
                relative_base += param1
                index += 2
    return output_arr, index, relative_base, memory, main_run

def calc_next_coordinate(x,y,dir, turn):
    if dir == 0:
        if turn == 0:
            x -= 1
        elif turn == 1:
            x += 1
    elif dir == 1:
        if turn == 0:
            y += 1
        elif turn == 1:
            y -= 1
    elif dir == 2:
        if turn == 0:
            x += 1
        elif turn == 1:
            x -= 1
    elif dir == 3:
        if turn == 0:
            y -= 1
        elif turn == 1:
            y += 1

    return x,y

def get_limits(pos):
    x_max = 0
    y_max = 0
    x_min = 0
    y_min = 0

    length = len(pos)

    for i in range(0,length):
        x_check = pos[i][0]
        y_check = pos[i][1]
        if x_check < x_min:
            x_min = x_check
        elif x_check > x_max:
            x_max = x_check
        if y_check < y_min:
            y_min = y_check
        elif y_check > y_max:
            y_max = y_check

    return x_min, x_max, y_min, y_max

def get_figure_matrix(limits, pos):
    width = limits[1] - limits[0] + 1
    height = limits[3] - limits[2] + 1

    matrix = np.zeros((height, width))
    w = len(matrix[0])
    h = len(matrix)

    for i in range(0, len(pos)):
        x = pos[i][0] - limits[0]
        y = pos[i][1] - limits[2]
        color = pos[i][2]
        matrix[y][x] = color

    for j in range(height - 1, -1, -1):
        for k in range(0, width):
            temp = matrix[j][k]
            if temp == 0:
                print("⬜", end='')
            elif temp == 1:
                print('⬛', end='')
        print()
    return matrix
def print_figure(matrix):
    cdict = {'red': ((0., 1, 1),
                     (0.05, 1, 1),
                     (0.11, 0, 0),
                     (0.66, 1, 1),
                     (0.89, 1, 1),
                     (1, 0.5, 0.5)),
             'green': ((0., 1, 1),
                       (0.05, 1, 1),
                       (0.11, 0, 0),
                       (0.375, 1, 1),
                       (0.64, 1, 1),
                       (0.91, 0, 0),
                       (1, 0, 0)),
             'blue': ((0., 1, 1),
                      (0.05, 1, 1),
                      (0.11, 1, 1),
                      (0.34, 1, 1),
                      (0.65, 0, 0),
                      (1, 0, 0))}

    my_cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap', cdict, 256)

    pcolor(matrix, cmap=my_cmap)
    colorbar()
    show()

def main():
    int_list = read()

    run = True
    index = 0
    relative_base = 0
    memory = {}
    in_data = 1

    x_pos = 0
    y_pos = 0

    pos = []
    count = 0
    # up = 0, right = 1, down = 2, left = 3
    direction = 0

    while run:
        full_output = run_operations(int_list, index, relative_base, memory, in_data)
        output = full_output[0]
        index = full_output[1]
        relative_base = full_output[2]
        memory = full_output[3]
        run = full_output[4]

        if run:
            color = output[0]
            turn = output[1]

            coordinate = [x_pos, y_pos, color]

            for i in range(0,len(pos)):
                x = pos[i][0]
                y = pos[i][1]

                if x == x_pos and y == y_pos:
                    pos[i][2] = color
                    break

                if i == (len(pos) - 1):
                    pos.append(coordinate)
                    count += 1
            if len(pos) == 0:
                pos.append(coordinate)
                count += 1
            next_cordinates = calc_next_coordinate(x_pos, y_pos, direction, turn)

            x_next = next_cordinates[0]
            y_next = next_cordinates[1]
            x_pos = x_next
            y_pos = y_next
            for i in range(0, len(pos)):
                x = pos[i][0]
                y = pos[i][1]

                if x == x_next and y == y_next:
                    in_data = pos[i][2]
                    break

                if i == (len(pos) - 1):
                    in_data = 0

            if turn == 0:
                direction -= 1
                if direction == -1:
                    direction = 3
            elif turn == 1:
                direction += 1
                direction = direction % 4

    limits = get_limits(pos)
    figure_matrix = get_figure_matrix(limits, pos)
    print_figure(figure_matrix)

    print("Total panels visited at least once is: " + str(count))

main()