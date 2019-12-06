def read():
    val = input()
    str_list = val.split(',')
    int_list = list(map(int,str_list))
    return int_list

def run_operations(int_list):


    run = True

    index = 0
    while run:
        opcode_str = str(int_list[index])
        length = len(opcode_str)
        if opcode_str == "99":
            run = False
        elif opcode_str[0] == '3' and length == 1:
            input_val = int(input("Set input"))
            input_index = int_list[index + 1]
            int_list[input_index] = input_val

            index += 2

        elif opcode_str[length - 1] == '4':
            mode_c_temp = '0'

            if length == 3:
                mode_c_temp = opcode_str[0]

            if mode_c_temp == '0':
                output_index = int_list[index + 1]
                print(int_list[output_index])
            else:
                print(int_list[index + 1])
            index += 2



        else:

            length = len(opcode_str)
            opcode_val = int(opcode_str[length - 1])

            mode_b = 0
            mode_c = 0

            if length == 4:
                mode_b = int(opcode_str[0])
                mode_c = int(opcode_str[1])
            elif length == 3:
                mode_c = int(opcode_str[0])
            int1 = 0
            int2 = 0
            int3 = 0
            sum = 0

            if mode_c == 0:
                index_int1 = int_list[index + 1]
                int1 = int_list[index_int1]
            else:
                int1 = int_list[index + 1]
            if mode_b == 0:
                index_int2 = int_list[index + 2]
                int2 = int_list[index_int2]
            else:
                int2 = int_list[index + 2]




            if opcode_val == 1:
                sum = int1 + int2
                int3 = int_list[index + 3]
                int_list[int3] = sum
                index += 4

            elif opcode_val == 2:
                sum = int1 * int2
                int3 = int_list[index + 3]
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
                int3 = int_list[index + 3]
                if int1 < int2:
                    int_list[int3] = 1
                else :
                    int_list[int3] = 0
                index += 4
            elif opcode_val == 8:
                int3 = int_list[index + 3]
                if int1 == int2:
                    int_list[int3] = 1
                else:
                    int_list[int3] = 0
                index += 4



    print(int_list)

def main():
    int_list = read()
    run_operations(int_list)


main()