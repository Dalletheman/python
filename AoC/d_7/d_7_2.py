def read():
    val = input()
    str_list = val.split(',')
    int_list = list(map(int,str_list))
    return int_list

def run_operations(int_list, input, phase_mode, index_in):

    output = 0
    run = True
    if index_in > 0:

        input_count = 1
    else:
        input_count = 0
    index = index_in
    main_run = True
    while run:
        opcode_str = str(int_list[index])
        length = len(opcode_str)
        if opcode_str == "99":
            run = False
            main_run = False
        elif opcode_str[0] == '3' and length == 1:
            input_val = 0
            if input_count == 0:
                input_val = phase_mode
            else:
                input_val = input

            input_index = int_list[index + 1]
            int_list[input_index] = input_val
            input_count += 1

            index += 2

        elif opcode_str[length - 1] == '4':
            mode_c_temp = '0'

            if length == 3:
                mode_c_temp = opcode_str[0]

            if mode_c_temp == '0':
                output_index = int_list[index + 1]
                output = int(int_list[output_index])
            else:
                output = int(int_list[index + 1])
            index += 2
            run = False


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



    return output, main_run, index
def phase_seq_gen():
    seq = [5,6,7,8,9]
    set_seq = []
    seq_array = []

    def seq_gen_inner(rem_seq,set_seq):


        if len(rem_seq) == 1:
            set_seq_temp = set_seq.copy()
            set_seq_temp.append(rem_seq[0])
            seq_array.append(set_seq_temp)
        else:
            for i in range(0,len(rem_seq)):
                rem_seq_temp = rem_seq.copy()
                set_seq_temp = set_seq.copy()
                rem_seq_temp.pop(i)
                set_seq_temp.append(rem_seq[i])

                seq_gen_inner(rem_seq_temp, set_seq_temp)

    seq_gen_inner(seq,set_seq)

    return seq_array


def main():
    int_list = read()
    phase_seq_collection = phase_seq_gen()
    max_thrust = 0
    for j in range(0, len(phase_seq_collection)):
        phase_seq = phase_seq_collection[j]
        input = 0
        output = 0
        last_e_output = 0
        list_a = int_list.copy()
        list_b = int_list.copy()
        list_c = int_list.copy()
        list_d = int_list.copy()
        list_e = int_list.copy()
        index1 = 0
        index2 = 0
        index3 = 0
        index4 = 0
        index5 = 0

        run = True
        i = 0
        while run:
            input = output
            if i == 0:
                out = run_operations(list_a, input, phase_seq[i],index1)
                output = out[0]
                index1 = out[2]
                if not out[1]:
                    run = False
            elif i == 1:
                out = run_operations(list_b, input, phase_seq[i], index2)
                output = out[0]
                index2 = out[2]
                if not out[1]:
                    run = False
            elif i == 2:
                out = run_operations(list_c, input, phase_seq[i], index3)
                output = out[0]
                index3 = out[2]
                if not out[1]:
                    run = False
            elif i == 3:
                out = run_operations(list_d, input, phase_seq[i], index4)
                output = out[0]
                index4 = out[2]
                if not out[1]:
                    run = False
            elif i == 4:
                out = run_operations(list_e, input, phase_seq[i], index5)
                output = out[0]
                index5 = out[2]
                last_e_output = output
                if not out[1]:
                    run = False
            i += 1
            if i == 5:
                i = 0

        if last_e_output > max_thrust:
            max_thrust = last_e_output
        print(j)
    print(max_thrust)
def maintest():
    int_list = read()
    max_thrust = 0

    phase_seq = [9,7,8,5,6]
    input = 0
    output = 0
    last_e_output = 0
    list_a = int_list.copy()
    list_b = int_list.copy()
    list_c = int_list.copy()
    list_d = int_list.copy()
    list_e = int_list.copy()
    index1 = 0
    index2 = 0
    index3 = 0
    index4 = 0
    index5 = 0

    run = True
    i = 0
    while run:
        input = output
        if i == 0:
            out = run_operations(list_a, input, phase_seq[i], index1)
            output = out[0]
            index1 = out[2]
            if not out[1]:
                run = False
        elif i == 1:
            out = run_operations(list_b, input, phase_seq[i], index2)
            output = out[0]
            index2 = out[2]
            if not out[1]:
                run = False
        elif i == 2:
            out = run_operations(list_c, input, phase_seq[i], index3)
            output = out[0]
            index3 = out[2]
            if not out[1]:
                run = False
        elif i == 3:
            out = run_operations(list_d, input, phase_seq[i], index4)
            output = out[0]
            index4 = out[2]
            if not out[1]:
                run = False
        elif i == 4:
            out = run_operations(list_e, input, phase_seq[i], index5)
            output = out[0]
            index5 = out[2]
            last_e_output = output
            if not out[1]:
                run = False
        i += 1
        if i == 5:
            i = 0


    print(last_e_output)

#phase_seq_gen()






main()
#maintest()