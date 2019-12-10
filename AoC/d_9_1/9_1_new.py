def read():
    val = input()
    str_list = val.split(',')
    int_list = list(map(int,str_list))
    return int_list

def run_operations(int_list):

    memory = {}
    total_length = len(int_list)
    index = 0
    relative_base = 0
    run = True

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
        # 3,4,9 has one param
        elif opcode_type == 3:
            input_val = int(input("Set input"))
            input_param = int_list[index + 1]
            if mode_c == 0:
                if input_param >= total_length:
                    input_param = input_param - total_length
                    memory[input_param] = input_val
                else:
                    memory[input_param] = input_val
            elif mode_c == 2:
                input_param = input_param + relative_base
                if input_param >= total_length:
                    input_param = input_param - total_length
                    memory[input_param] = input_val
                else:
                    memory[input_param] = input_val
            index += 2

        elif opcode_type == 4:
            output_param = int_list[index + 1]

            if mode_c == 0:
                if output_param >= total_length:
                    output_param = output_param - total_length
                    if memory.get(output_param) == None:
                        print(0)
                    else:
                        print(memory.get(output_param))
                else:
                    print(int_list[output_param])
            elif mode_c == 1:
                print(output_param)
            elif mode_c == 2:
                output_param = output_param + relative_base
                if output_param >= total_length:
                    output_param = output_param - total_length
                    if memory.get(output_param) == None:
                        print(0)
                    else:
                        print(memory.get(output_param))
                else:
                    print(int_list[output_param])
            index += 2
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



def main():
    int_list = read()
    run_operations(int_list)

main()