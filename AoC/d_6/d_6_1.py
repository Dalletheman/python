import sys

def readdata():
    with open('input1.txt') as f:
        data = f.read().splitlines()
    data = [item.split(')') for item in data]
    return data


def count_orbits_inner(data, id, depth):
    sum = 0

    for j in range(0, len(data)):
        if data[j][0] == id:
            next_id = data[j][1]
            sum = sum + count_orbits_inner(data, next_id, depth + 1)
    return sum + depth
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