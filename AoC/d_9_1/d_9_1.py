def read():
    val = input()
    str_list = val.split(',')
    int_list = list(map(int,str_list))
    return int_list

def run_operations(int_list):

    run = True
    memory = {}
    length_list = len(int_list)
    index = 0

    relative_base = 0
    while run:
        opcode_str = str(int_list[index])
        length = len(opcode_str)
        # opcode 99 will end the loop
        if opcode_str == "99":
            run = False
        # opcode 3 is a input code

        elif opcode_str[length - 1] == '3':
            input_val = int(input("Set input"))
            input_index = int_list[index + 1]
            if length == 3:
                mode_c_temp = opcode_str[0]
                if mode_c_temp == '2':
                    input_index = input_index + relative_base
                    if input_index > length:
                        input_index = input_index - length_list
                        memory[input_index] = input_val
                    else:
                        int_list[input_index] = input_val

            else:
                if input_index > length:
                    memory[input_index] = input_val
                else:
                    int_list[input_index] = input_val

            index += 2
        # opcode 4 is a output code
        #
        elif opcode_str[length - 1] == '4':
            mode_c_temp = '0'
            # checks the mode
            if length == 3:
                mode_c_temp = opcode_str[0]
            # if the mode is 0 the value is taken from index
            # if the index is higher than total length of data the value is taken from memory
            if mode_c_temp == '0':
                output_index = int_list[index + 1]
                if output_index > length_list:
                    new_index = output_index - length_list
                    if memory.get(new_index) == None:
                        print(0)
                    else:
                        print(memory.get(new_index))
                else:
                    print(int_list[output_index])
            # if the mode is 1 value is taken directly
            elif mode_c_temp == '1':
                print(int_list[index + 1])
            # if the mode is 2 value is taken from index
            # if hte index is higher than total length of data the value is taken from memory
            elif mode_c_temp == '2':
                output_index = int_list[index + 1] + relative_base
                if output_index > length_list:
                    new_index = output_index - length_list
                    if memory.get(new_index) == None:
                        print(0)
                    else:
                        print(memory.get(new_index))
                else:
                    print(int_list[output_index])

            index += 2
        # all other opcodes
        else:

            length = len(opcode_str)
            opcode_val = int(opcode_str[length - 1])

            mode_a = 0
            mode_b = 0
            mode_c = 0

            if length == 4:
                mode_b = int(opcode_str[0])
                mode_c = int(opcode_str[1])
            elif length == 3:
                mode_c = int(opcode_str[0])
            elif length == 5:
                mode_a = int(opcode_str[0])
                mode_b = int(opcode_str[1])
                mode_c = int(opcode_str[2])

            int1 = 0
            int2 = 0
            int3 = 0
            sum = 0

            if mode_c == 0:
                index_int1 = int_list[index + 1]
                if index_int1 > length_list:
                    new_index = index_int1 - length_list
                    if memory.get(new_index) == None:
                        int1 = 0
                    else:
                        int1 = memory.get(new_index)
                else:
                    int1 = int_list[index_int1]
            elif mode_c == 1:
                int1 = int_list[index + 1]

            elif mode_c == 2:
                index_int1 = int_list[index + 1] + relative_base
                if index_int1 > length_list:
                    new_index = index_int1 - length_list
                    if memory.get(new_index) == None:
                        int1 = 0
                    else:
                        int1 = memory.get(new_index)
                else:
                    int1 = int_list[index_int1]
            # opcode 9 only has one parameter all other has 2
            if opcode_val != 9:

                if mode_b == 0:
                    index_int2 = int_list[index + 2]
                    if index_int2 > length_list:
                        new_index = index_int2 - length_list
                        if memory.get(new_index) == None:
                            int2 = 0
                        else:
                            int2 = memory.get(new_index)
                    else:
                        int2 = int_list[index_int1]
                elif mode_b == 1:
                    int2 = int_list[index + 2]
                elif mode_b == 2:
                    index_int2 = int_list[index + 1] + relative_base
                    if index_int2 > length_list:
                        new_index = index_int2 - length_list
                        memory[new_index] = sum
                    else:
                        int2 = int_list[index_int1]
            # adds together int1 and int2, the sum is placed in index int3
            if opcode_val == 1:
                sum = int1 + int2
                if mode_a != 2:
                    int3 = int_list[index + 3]
                    if int3 > length_list:
                        new_index = int3 - length_list
                        memory[new_index] = sum

                    else:
                        int_list[int3] = sum
                else:
                    int3 = int_list[index + 3] + relative_base
                    if int3 > length_list:
                        new_index = int3 - length_list
                        memory[new_index] = sum

                    else:
                        int_list[int3] = sum

                index += 4

            elif opcode_val == 2:
                sum = int1 * int2
                if mode_a != 2:


                    int3 = int_list[index + 3]

                    if int3 > length_list:
                        new_index = int3 - length_list
                        memory[new_index] = sum
                    else:
                        int_list[int3] = sum
                else:
                    int3 = int_list[index + 3] + relative_base

                    if int3 > length_list:
                        new_index = int3 - length_list
                        memory[new_index] = sum
                    else:
                        int_list[int3] = sum


                index += 4
            elif opcode_val == 5:

                if int1 != 0:
                    index = int2
                else:
                    index += 3
            elif opcode_val == 6:
                if int1 == 0:
                    index = int2
                else:
                    index += 3
            elif opcode_val == 7:
                if mode_a != 2:

                    int3 = int_list[index + 3]
                    if int1 < int2:
                        if int3 > length_list:
                            new_index = int3 - length_list
                            memory[new_index] = 1
                        else:
                            int_list[int3] = 1
                    else :
                        if int3 > length_list:
                            new_index = int3 - length_list
                            memory[new_index] = 0
                        else:
                            int_list[int3] = 0
                else:
                    int3 = int_list[index + 3] + relative_base
                    if int1 < int2:
                        if int3 > length_list:
                            new_index = int3 - length_list
                            memory[new_index] = 1
                        else:
                            int_list[int3] = 1
                    else:
                        if int3 > length_list:
                            new_index = int3 - length_list
                            memory[new_index] = 0
                        else:
                            int_list[int3] = 0
                index += 4
            elif opcode_val == 8:
                if mode_a != 2:

                    int3 = int_list[index + 3]
                    if int1 == int2:
                        if int3 > length_list:
                            new_index = int3 - length_list
                            memory[new_index] = 1
                        else:
                            int_list[int3] = 1
                    else:
                        if int3 > length_list:
                            new_index = int3 - length_list
                            memory[new_index] = 0
                        else:
                            int_list[int3] = 0
                else:
                    int3 = int_list[index + 3] + relative_base
                    if int1 == int2:
                        if int3 > length_list:
                            new_index = int3 - length_list
                            memory[new_index] = 1
                        else:
                            int_list[int3] = 1
                    else:
                        if int3 > length_list:
                            new_index = int3 - length_list
                            memory[new_index] = 0
                        else:
                            int_list[int3] = 0
                index += 4
            elif opcode_val == 9:
                relative_base += int1
                index += 2



    print(int_list)

def main():
    int_list = read()
    run_operations(int_list)



main()