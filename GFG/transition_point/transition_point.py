# your task is to complete this function
# finvtion should return an integer
def transitionPoint(arr, n):
    si = 0
    ei = n - 1
    final_index = -1

    run = True
    while run:
        if si == ei - 1:
            run = False
            final_index = si
        else:
            mid = si + ((ei - si)//2)
            if arr[mid] == 1:
                ei = mid
            else:
                si = mid
    return final_index + 1

#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))

        print(transitionPoint(arr, n))
# Contirbuted By: Harshit Sidhwa
# } Driver Code Ends