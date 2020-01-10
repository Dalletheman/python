def read():
    val = input()
    str_list = val.split(',')
    int_list = list(map(int,str_list))
    return int_list

def run_operations(int_list, in_index, in_relative_base, in_memory, input):

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
            input_val = input
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
            if len(output_arr) == 1:
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

def in_list(positions, pos):

    length = len(positions)
    for i in range(0, length):
        if pos[0] == positions[i][0][0] and pos[1] == positions[i][0][1]:
            return True

    return False


def create_matrix(limits):
    width = limits[1] - limits[0] + 1
    height = limits[3] - limits[2] + 1
    row = ['⬛'] * width
    matrix = []

    for i in range(0, height):
        matrix.append(row.copy())

    return matrix


def get_limits(positions):
    x_low = 0
    x_high = 0
    y_low = 0
    y_high = 0

    length = len(positions)

    for i in range(0,length):
        x_temp = positions[i][0][0]
        y_temp = positions[i][0][1]

        if x_temp < x_low:
            x_low = x_temp
        elif x_temp > x_high:
            x_high = x_temp
        elif y_temp < y_low:
            y_low = y_temp
        elif y_temp > y_high:
            y_high = y_temp

    return [x_low, x_high, y_low, y_high]

def fill_matrix(positions, matrix, x_low, y_low):



    for i in range(0, len(positions)):
        x = positions[i][0][0] + abs(x_low)
        y = positions[i][0][1] + abs(y_low)
        val = positions[i][1]
        matrix[y][x] = val

        if val == 'G':
            print('stop')
    return matrix

def print_matrix(filled_matrix):
    width = len(filled_matrix[0])
    height = len(filled_matrix)

    for i in range(0,height):
        for j in range(0,width):
            print(filled_matrix[i][j], end='')
        print('')



def main():
    int_list = read()
    index = 0
    relative_base = 0
    memory = {}
    positions = []
    init_pos = [0,0]
    run = True
    count = 0


    def inner_main(int_list_copy, index, relative_base, memory_copy, pos, counter):

        for i in range(1,5):
            temp_counter = counter
            int_list_input = int_list_copy.copy()
            memory_input = memory_copy.copy()
            new_pos = pos.copy()
            input = i
            if i == 1:
                new_pos[1] += 1
            elif i == 2:
                new_pos[1] -= 1
            elif i == 3:
                new_pos[0] -= 1
            elif i == 4:
                new_pos[0] += 1
            if not in_list(positions, new_pos):
                output = run_operations(int_list_input, index, relative_base, memory_input, input)
                output_val = output[0][0]
                temp_index = output[1]
                temp_relative_base = output[2]
                memory_input = output[3]

                if output_val == 0:
                    coordinate = [new_pos, '⬛']
                    positions.append(coordinate)
                elif output_val == 1:
                    temp_counter += 1
                    coordinate = [new_pos, '⬜']
                    positions.append(coordinate)
                    inner_main(int_list_input, temp_index, temp_relative_base, memory_input, new_pos, temp_counter)
                elif output_val == 2:
                    coordinate = [new_pos, '⬜']
                    positions.append(coordinate)
                    print('Hej')
                    print(counter + 1)

    inner_main(int_list.copy(), index, relative_base, memory.copy(), init_pos, count)


    limit = get_limits(positions)
    matrix = create_matrix(limit)

    x_low = limit[0]
    y_low = limit[2]


    filled_matrix = fill_matrix(positions, matrix, x_low, y_low)
    filled_matrix[abs(y_low)][abs(x_low)] = '⬜'

    print_matrix(filled_matrix)





main()