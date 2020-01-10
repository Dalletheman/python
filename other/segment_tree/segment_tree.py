import math

def find_sum(st, ss, se, qs, qe, insert_index):
    if qe < ss or qs > se:
        return 0
    elif qs <= ss and qe >= se:
        return st[insert_index]
    else:
        mid = ss + ((se - ss) // 2)
        return find_sum(st, ss, mid, qs, qe, 2*insert_index + 1) + find_sum(st, mid + 1, se, qs, qe, 2*insert_index + 2)


def construct_st(input, length):
    height = math.ceil(math.log(length, 2))
    size = 2*pow(2,height) - 1
    st = [0] * size
    build_st(input, st, 0, length - 1, 0)
    return st


def build_st(input, st, start_i, end_i, insert_index):
    if start_i == end_i:
        st[insert_index] = input[start_i]
        return input[start_i]
    else:
        mid_i = start_i + ((end_i - start_i) // 2)
        st[insert_index] = build_st(input, st, start_i, mid_i, 2*insert_index + 1) + build_st(input, st, mid_i + 1, end_i, 2*insert_index + 2)
        return st[insert_index]


def main():
    input = [1, 3, 5, 7, 9, 11]

    length = len(input)
    seg_tree = construct_st(input, length)

    qs = 2
    qe = 4

    sum = find_sum(seg_tree, 0, length - 1, qs, qe, 0)

    print(seg_tree)
    print(sum)




if __name__ == '__main__':
    main()