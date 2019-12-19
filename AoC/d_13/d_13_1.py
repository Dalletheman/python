def read():
    val = input()
    str_list = val.split(',')
    int_list = list(map(int,str_list))
    return int_list

def run_operations(int_list, in_index, in_relative_base, in_memory):

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
            input_val = 0
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
            if len(output_arr) == 3:
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

def make_matrix(x,y):

    matrix = []
    for i in range(0,y):
        zeros_list = [0] * x
        matrix.append(zeros_list)

    return matrix

def count_blocks(matrix):
    y = len(matrix)
    x = len(matrix[0])

    count = 0
    for i in range(0, y):
        for j in range(0, x):
            if matrix[i][j] == 2:
                count += 1
    return count

def print_matrix(matrix):
    y = len(matrix)
    x = len(matrix[0])

    for i in range(0, y):
        for j in range(0, x):
            print(matrix[i][j], end='')
        print()


def main():
    int_list = read()
    index = 0
    relative_base = 0
    memory = {}
    # make grid
    matrix = make_matrix(44,24)

    run = True
    x_max = 0
    y_max = 0
    while run:

        output = run_operations(int_list, index, relative_base, memory)
        index = output[1]
        relative_base = output[2]
        memory = output[3]
        if output[4]:
            x = output[0][0]
            y = output[0][1]
            id = output[0][2]

            matrix[y][x] = id
            if x > x_max:
                x_max = x
            if y > y_max:
                y_max = y
        else:
            run = False
        #print(output[0])
    print_matrix(matrix)
    print(count_blocks(matrix))
    print("x: " + str(x_max))
    print("y: " + str(y_max))




main()