
def facing_sun(arr, n):
    count = 1
    highest = arr[0]
    for i in range(1, n):
        if arr[i] > highest:
            count += 1
            highest = arr[i]

    return count



if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))

        print(facing_sun(arr, n))