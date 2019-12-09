def read():
    with open('input2.txt') as f:
        data = f.read().splitlines()
    return data

def calc_layer_value(data, index, layer_length):
    n_1 = 0
    n_2 = 0

    start_index = index * layer_length
    end_index = start_index + layer_length

    sub_string = data[start_index:end_index]

    for i in range(0,len(sub_string)):
        if sub_string[i] == '1':
            n_1 += 1
        elif sub_string[i] == '2':
            n_2 += 1

    return n_1*n_2

def main():
    data = read()[0]

    data_length = len(data)
    width = 25
    heigth = 6

    layer_length = width * heigth

    n_layers = data_length // layer_length
    min_count = 10000
    min_count_index = 0
    for i in range(0, n_layers):
        start_index = layer_length * i
        end_index = start_index + layer_length
        sub_string = data[start_index:end_index]
        count = 0
        for j in range(0,layer_length):
            if sub_string[j] == '0':
                count += 1
        if count < min_count:
            min_count = count
            min_count_index = i
    value = calc_layer_value(data, min_count_index, layer_length)
    print(value)



main()

