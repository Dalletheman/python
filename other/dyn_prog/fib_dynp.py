## fibonacci dynamic programming solution with memoization


def init(n):
    a = [0,1];

    for i in range(0,n - 2):
        a.append(-1)
    return a
def fib(n):

    if a[n] != -1:
        return a[n]
    else:
        a[n] = fib(n - 1) + fib(n - 2)
        return a[n]

n = 7

a = init(n)
print(fib(n - 1))


