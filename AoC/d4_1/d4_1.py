def check(value):

    str_value = str(value)

    prev_value = int(str_value[0])
    check_adjacent = False
    check_size = True
    prev_adjacent = False
    for i in range(1,6):
        current_value = int(str_value[i])
        if prev_value == current_value:
            if not prev_adjacent and i == 5:
                check_adjacent = True
            if prev_adjacent:
                prev_adjacent = False
            else:
                prev_adjacent = True
        elif prev_adjacent:
            check_adjacent = True
            prev_adjacent = False
        if prev_value > current_value:
            check_size = False
        prev_value = current_value



    return check_adjacent and check_size

def main():
    low = 125730

    high = 579381

    count = 0



    print(check(112233))
    print(check(122444))
    print(check(111111))


    for i in range(low,high + 1):
        if check(i):
            count += 1

    print(count)




main()