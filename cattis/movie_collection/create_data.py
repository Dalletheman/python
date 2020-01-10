import random


f = open('test_sample.txt', 'w')
n = random.randrange(5,10)
f.write(str(n) + '\n')

for i in range(0,n):

    m = random.randrange(1,100)
    r = random.randrange(1,100)
    f.write(str(m) + ' ' + str(r) + '\n')
    for j in range(0,r):
        a = random.randrange(1,m + 1)
        f.write(str(a))
        if j < r - 1:
            f.write(' ')
    f.write('\n')





