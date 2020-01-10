import sys

def readdata(input):
    if input:
        data = sys.stdin.read().splitlines()
    else:
        with open('test_sample.txt') as f:
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

def main():
    data = list_2_matrix(readdata(False))
    n = data[0][0]

    for i in range(0,n):
        seen = []
        stack = []
        stack_size = data[i*2 + 1][0]
        n_requests = data[i*2 + 1][1]

        for s in range(1, stack_size + 1):
            stack.append(s)

        movie_id = data[i*2 + 2]

        for j in range(0,n_requests):
            id = movie_id[j]
            if id in seen:
                id_index = seen.index(id)
                seen.pop(id_index)
                seen.insert(0, id)

                print(id_index, end='')
            else:
                seen_size = len(seen)
                id_stack = stack.index(id)
                n_above = seen_size + id_stack
                print(n_above, end='')
                seen.insert(0, id)
                stack.pop(id_stack)
            print(' ', end='')
        print('')






main()