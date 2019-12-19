import math
def readdata():
    with open('input1.txt') as f:
        data = f.read().splitlines()
    return data

def calc_vel(pos, vel):


    for i in range(0, 3):

        for j in range(i + 1, 4):
            x1 = pos[i][0]
            y1 = pos[i][1]
            z1 = pos[i][2]
            x2 = pos[j][0]
            y2 = pos[j][1]
            z2 = pos[j][2]

            if x1 < x2:
                vel[i][0] += 1
                vel[j][0] -= 1
            elif x2 < x1:
                vel[i][0] -= 1
                vel[j][0] += 1
            if y1 < y2:
                vel[i][1] += 1
                vel[j][1] -= 1
            elif y2 < y1:
                vel[i][1] -= 1
                vel[j][1] += 1
            if z1 < z2:
                vel[i][2] += 1
                vel[j][2] -= 1
            elif z2 < z1:
                vel[i][2] -= 1
                vel[j][2] += 1
    return vel
def calc_pos(pos, vel):

    for i in range(0,len(pos)):
        pos[i][0] += vel[i][0]
        pos[i][1] += vel[i][1]
        pos[i][2] += vel[i][2]

    return pos

def calc_power(pos, vel):
    power = 0

    for i in range(0,len(pos)):
        pot = abs(pos[i][0]) + abs(pos[i][1]) + abs(pos[i][2])
        kin = abs(vel[i][0]) + abs(vel[i][1]) + abs(vel[i][2])

        power += (pot*kin)

    return power

def print_vel_diff(vel, prev_vel):

    for i in range(0, len(vel)):
        x_diff = vel[i][0] - prev_vel[i][0]
        y_diff = vel[i][1] - prev_vel[i][1]
        z_diff = vel[i][2] - prev_vel[i][2]

        vel_diff = [x_diff, y_diff, z_diff]

        print(vel_diff)
    print()

def next_prime(n):


    run = True
    while run:
        n += 1
        limit = int(math.sqrt(n)) + 1
        if limit < 2:
            run = False
        elif n % 2 != 0:
            i = 2
            while i < limit + 1:
                if i == limit:
                    run = False
                i += 1
                if n % i == 0:
                    break

    return n




def calc_gcd(x):



    prime_factors = []

    shortest_index = 0
    shortest_length = 10000
    for i in range(0,2):
        x_prime = []
        rest = x[i]
        run = True

        prime_num = 2

        count_n = 0
        while run:

            prime_val = prime_num
            if rest % prime_val == 0:
                x_prime.append(prime_val)
                rest = rest / prime_val
                count_n += 1
            else:
                prime_num = next_prime(prime_num)
            if rest == 1:
                run = False

        if count_n < shortest_length:
            shortest_length = count_n
            shortest_index = i
        prime_factors.append(x_prime)

    i1 = shortest_index
    i0 = shortest_index - 1
    if i0 == -1:
        i0 = 1


    common_primes = []
    for i in range(0,shortest_length):
        value = prime_factors[i1][i]

        if value in prime_factors[i0]:
            common_primes.append(value)
            index_i0 = prime_factors[i0].index(value)
            prime_factors[i0].pop(index_i0)


    gcd = 1
    for i in range(0, len(common_primes)):
        gcd *= common_primes[i]

    return gcd



def calc_lcm_pair(x):

    denominator = calc_gcd(x)
    nominator = abs(x[0]*x[1])

    return nominator / denominator




def calc_lcm(period):
    x1 = period[0]
    x2 = period[1]
    x3 = period[2]


    lcm1 = calc_lcm_pair([x1, x2])
    lcm2 = calc_lcm_pair([x2, x3])

    final_lcm = calc_lcm_pair([lcm1, lcm2])
    return final_lcm




def main():
    data = readdata()
    #print(data)
    pos = [[-8, -10, 0], [5, -5, 10], [2, -7, 3], [9, -8, -3]]
    vel = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    pos_init = [[-7, -8, 9], [-12, -3, -4], [6, -17, -9], [4, -10, -6]]

    period = []
    for n in range(0,3):
        pos = [[-7, -8, 9], [-12, -3, -4], [6, -17, -9], [4, -10, -6]]
        vel = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

        run = True
        count = 0
        while run:
            vel = calc_vel(pos, vel)
            pos = calc_pos(pos, vel)
            if pos[0][n] == pos_init[0][n] and pos[1][n] == pos_init[1][n] and pos[2][n] == pos_init[2][n] and pos[3][n] == pos_init[3][n]:
                period.append(count + 2)
                run = False
            count += 1

    print(period)
    print(calc_lcm(period))




main()
