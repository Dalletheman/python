import sys



def readdata(input):
    if input:
        data = sys.stdin.read().splitlines()
    else:
        with open('4.txt') as f:
            data = f.read().splitlines()
    return data
def list_2_matrix(str_list):
    matrix = []
    length = len(str_list)
    for i in range(0, length):
        temp = str_list[i].split(' ')
        temp = list(map(int, temp))
        matrix.append(temp)
    return matrix

def internet_connection(data):
    n_houses = data[0][0]
    n_cables = data[0][1]

    unions = []

    for i in range(1, n_cables + 1):
        a = data[i][0]
        b = data[i][1]
        unions_length = len(unions)

        if unions_length == 0:
            new_union = [a, b]
            unions.append(new_union)
        else:
            #a = data[i][0]
            #b = data[i][1]
            union_merge = []
            add_a = False
            add_b = False
            for j in range(0, unions_length):
                a_match = False
                b_match = False
                if a in unions[j]:
                    a_match = True
                    add_b = True
                if b in unions[j]:
                    b_match = True
                    add_a = True
                if a_match or b_match:
                    union_merge.append(j)

            length_merge = len(union_merge)

            if length_merge == 1:
                if not (add_a and add_b):
                    if add_a:
                        unions[union_merge[0]].append(a)
                    else:
                        unions[union_merge[0]].append(b)
            elif length_merge == 0:
                new_union = [a, b]
                unions.append(new_union)
            else:
                length_union_1 = len(unions[union_merge[0]])
                length_union_2 = len(unions[union_merge[1]])

                if length_union_1 > length_union_2:
                    for k in range(0, length_union_2):
                        unions[union_merge[0]].append(unions[union_merge[1]][k])
                    unions.pop(union_merge[1])
                else:
                    for k in range(0, length_union_1):
                        unions[union_merge[1]].append(unions[union_merge[0]][k])
                    unions.pop(union_merge[0])

    return unions



if __name__=='__main__':
    data = list_2_matrix(readdata(True))

    unions = internet_connection(data)

    unions_length = len(unions)
    connected = False

    rest = []
    for i in range(0, unions_length):
        if 1 in unions[i]:
            connected = True
        else:
            length = len(unions[i])

            for j in range(0, length):
                rest.append(unions[i][j])

            unions.pop(i)

    if connected and unions_length == 1:
        print('Connected')
    elif not connected and unions_length == 1:
        rest.sort()
        n_houses = data[0][0]
        rest_index = 0
        rest_length = len(rest)
        for i in range(1, n_houses + 1):
            rest_val = rest[rest_index]
            if rest_val == i:
                print(rest_val)
                if rest_index < rest_length - 1:
                    rest_index += 1
            else:
                if i != 1:
                    print(i)

    else:
        unions[0].sort()
        rest.sort()
        n_houses = data[0][0]
        rest_index = 0
        rest_length = len(rest)
        unions_index = 0
        union_length = len(unions[0])
        for i in range(1, n_houses + 1):
            rest_val = rest[rest_index]
            unions_val = unions[0][unions_index]
            if rest_val == i or unions_val == i:
                if rest_val == i:
                    print(rest_val)
                    if rest_index < rest_length - 1:
                        rest_index += 1
                elif unions_val == i and unions_index < union_length - 1:
                    unions_index += 1
            else:
                print(i)
