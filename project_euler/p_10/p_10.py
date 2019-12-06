import math


def check_prime(n):
    limit = int(math.sqrt(n))

    for i in range(2,limit + 1):
        if n % i == 0:
            return False
    return True
def sum_primes(n):
    sum = 0

    if n > 1:
        sum = 2
        for i in range(3,n - 1):
            if check_prime(i):
                sum = sum + i
    return sum
n = 2000000;
print(sum_primes(n))





