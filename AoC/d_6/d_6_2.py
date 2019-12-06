import sys

def readdata():
    with open('input1.txt') as f:
        data = f.read().splitlines()
    data = [item.split(')') for item in data]
    return data


def count_orbits_inner(data, id, depth):
    sum = 0

    count = 0

    if id == "YOU" or id == "SAN":
        sum = depth - 1
    else:
        for j in range(0, len(data)):
            if data[j][0] == id:
                next_id = data[j][1]
                temp_sum = count_orbits_inner(data, next_id, depth + 1)
                sum = sum + temp_sum
                if temp_sum > 0:
                    count += 1

        if count == 2:
            sum = sum - depth * 2
    return sum
def count_orbits(data):

    com_index = 0
    for i in range(0, len(data)):
        if data[i][0] == "COM":
            com_index = i
            break
    fin_sum = count_orbits_inner(data,data[com_index][1], 1)
    return fin_sum



def test(a):
    def add(b):
        nonlocal a
        a += 1
        return a + b

    return add




def main():
    data = readdata()
    n = count_orbits(data)
    print(n)



main()