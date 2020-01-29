class intcomputer:
    def __init__(self, intcode):
        self.intcode = intcode
        self.memory = {}
        self.index = 0
        self.relative_base = 0
        self.total_length = len(intcode)

    def run(self):
        output_arr = []
        run = True
        main_run = True
        while run:
            opcode = str(self.intcode[self.index])
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
                input_val = int(input('Input'))
                input_param = self.intcode[self.index + 1]
                if mode_c == 0:
                    if input_param >= self.total_length:
                        input_param = input_param - self.total_length
                        self.memory[input_param] = input_val
                    else:
                        self.intcode[input_param] = input_val
                elif mode_c == 2:
                    input_param = input_param + self.relative_base
                    if input_param >= self.total_length:
                        input_param = input_param - self.total_length
                        self.memory[input_param] = input_val
                    else:
                        self.intcode[input_param] = input_val
                self.index += 2

            elif opcode_type == 4:
                output_param = self.intcode[self.index + 1]
                output = 0
                if mode_c == 0:
                    if output_param >= self.total_length:
                        output_param = output_param - self.total_length
                        if self.memory.get(output_param) == None:
                            output = 0
                        else:
                            output = self.memory.get(output_param)
                    else:
                        output = self.intcode[output_param]
                elif mode_c == 1:
                    output = output_param
                elif mode_c == 2:
                    output_param = output_param + self.relative_base
                    if output_param >= self.total_length:
                        output_param = output_param - self.total_length
                        if self.memory.get(output_param) == None:
                            output = 0
                        else:
                            output = self.memory.get(output_param)
                    else:
                        output = self.intcode[output_param]

                output_arr.append(output)

                self.index += 2
                if len(output_arr) == 1:
                    run = False
            else:

                param1 = self.intcode[self.index + 1]
                param2 = 0
                param3 = 0
                if mode_c == 0:
                    if param1 >= self.total_length:
                        param1 = param1 - self.total_length
                        if self.memory.get(param1) == None:
                            param1 = 0
                        else:
                            param1 = self.memory.get(param1)
                    else:
                        param1 = self.intcode[param1]
                elif mode_c == 2:
                    param1 = param1 + self.relative_base
                    if param1 >= self.total_length:
                        param1 = param1 - self.total_length
                        if self.memory.get(param1) == None:
                            param1 = 0
                        else:
                            param1 = self.memory.get(param1)
                    else:
                        param1 = self.intcode[param1]

                if opcode_type != 9:

                    if mode_b == 0:
                        param2_index = self.intcode[self.index + 2]
                        if param2_index >= self.total_length:
                            param2_index = param2_index - self.total_length
                            if self.memory.get(param2_index) == None:
                                param2 = 0
                            else:
                                param2 = self.memory.get(param2_index)
                        else:
                            param2 = self.intcode[param2_index]
                    elif mode_b == 1:
                        param2 = self.intcode[self.index + 2]
                    elif mode_b == 2:
                        param2_index = self.intcode[self.index + 2] + self.relative_base
                        if param2_index >= self.total_length:
                            param2_index = param2_index - self.total_length
                            if self.memory.get(param2_index) == None:
                                param2 = 0
                            else:
                                param2 = self.memory.get(param2_index)
                        else:
                            param2 = self.intcode[param2_index]

                if opcode_type == 1:
                    sum = param1 + param2
                    if mode_a == 0:
                        param3 = self.intcode[self.index + 3]
                        if param3 >= self.total_length:
                            new_index = param3 - self.total_length
                            self.memory[new_index] = sum
                        else:
                            self.intcode[param3] = sum
                    elif mode_a == 2:
                        param3 = self.intcode[self.index + 3] + self.relative_base
                        if param3 >= self.total_length:
                            new_index = param3 - self.total_length
                            self.memory[new_index] = sum
                        else:
                            self.intcode[param3] = sum
                    self.index += 4

                elif opcode_type == 2:
                    sum = param1 * param2
                    if mode_a == 0:
                        param3 = self.intcode[self.index + 3]
                        if param3 >= self.total_length:
                            new_index = param3 - self.total_length
                            self.memory[new_index] = sum
                        else:
                            self.intcode[param3] = sum
                    elif mode_a == 2:
                        param3 = self.intcode[self.index + 3] + self.relative_base
                        if param3 >= self.total_length:
                            new_index = param3 - self.total_length
                            self.memory[new_index] = sum
                        else:
                            self.intcode[param3] = sum
                    self.index += 4

                elif opcode_type == 5:

                    if param1 != 0:
                        self.index = param2
                    else:
                        self.index += 3

                elif opcode_type == 6:
                    if param1 == 0:
                        self.index = param2
                    else:
                        self.index += 3

                elif opcode_type == 7:

                    if mode_a == 0:
                        param3 = self.intcode[self.index + 3]
                        if param1 < param2:
                            if param3 >= self.total_length:
                                new_index = param3 - self.total_length
                                self.memory[new_index] = 1
                            else:
                                self.intcode[param3] = 1
                        else:
                            if param3 >= self.total_length:
                                new_index = param3 - self.total_length
                                self.memory[new_index] = 0
                            else:
                                self.intcode[param3] = 0
                    elif mode_a == 2:
                        param3 = self.intcode[self.index + 3] + self.relative_base
                        if param1 < param2:
                            if param3 >= self.total_length:
                                new_index = param3 - self.total_length
                                self.memory[new_index] = 1
                            else:
                                self.intcode[param3] = 1
                        else:
                            if param3 >= self.total_length:
                                new_index = param3 - self.total_length
                                self.memory[new_index] = 0
                            else:
                                self.intcode[param3] = 0

                    self.index += 4

                elif opcode_type == 8:

                    if mode_a == 0:
                        param3 = self.intcode[self.index + 3]
                        if param1 == param2:
                            if param3 >= self.total_length:
                                new_index = param3 - self.total_length
                                self.memory[new_index] = 1
                            else:
                                self.intcode[param3] = 1
                        else:
                            if param3 >= self.total_length:
                                new_index = param3 - self.total_length
                                self.memory[new_index] = 0
                            else:
                                self.intcode[param3] = 0
                    elif mode_a == 2:
                        param3 = self.intcode[self.index + 3] + self.relative_base
                        if param1 == param2:
                            if param3 >= self.total_length:
                                new_index = param3 - self.total_length
                                self.memory[new_index] = 1
                            else:
                                self.intcode[param3] = 1
                        else:
                            if param3 >= self.total_length:
                                new_index = param3 - self.total_length
                                self.memory[new_index] = 0
                            else:
                                self.intcode[param3] = 0
                    self.index += 4

                elif opcode_type == 9:
                    self.relative_base += param1
                    self.index += 2
        return output_arr, main_run

def read():
    #val = input()
    f = open('test_2.txt', 'r')
    val = f.readline()
    str_list = val.split(',')
    int_list = list(map(int,str_list))
    return int_list

def print_matrix(matrix):
    width = len(matrix[0])
    height = len(matrix) - 1

    for i in range(0, height):
        for j in range(0, width):
            print(matrix[i][j], end='')
        print('')

def check_intersections(matrix):
    width = len(matrix[0])
    height = len(matrix) - 1
    sum = 0
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if matrix[i][j] == '#':
                top = matrix[i - 1][j]
                right = matrix[i][j + 1]
                down = matrix[i + 1][j]
                left = matrix[i][j - 1]
                if top == right == down == left == '#':
                    sub_sum = (i) * (j)
                    sum += sub_sum
    return sum
#main: A, B, A, B, A, C, B, C, A, C
# A: R, 4, L, 10, L, 10
# B: L, 8, R, 12, R, 10, R, 4
# C: L, 8, L, 8, R, 10, R, 4

def main_2():
    print(ord('󅆘'))
    intcode = read()
    int_comp = intcomputer(intcode)
    running = True
    image_matrix = []
    image_array = []
    while running:

        output_arr = int_comp.run()
        out = output_arr[0]
        running = output_arr[1]
        if not running:
            break
        else:
            if out[0] == 10:
                image_matrix.append(image_array)
                image_array = []
                print('')
            elif out[0] == 35:
                image_array.append('#')
                print('#', end='')
            elif out[0] == 46:
                image_array.append('.')
                print('.', end='')
            elif out[0] == 94:
                image_array.append('^')
                print('^', end='')
            else:
                print(chr(out[0]), end='')


main_2()