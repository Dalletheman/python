def read():
    with open('input2.txt') as f:
        data = f.read().splitlines()
    return data


def print_image(final_image, width, height):

    for i in range(0,height):
        start_index = i * width
        end_index = start_index + width
        sub_image = final_image[start_index:end_index]
        print(sub_image)

def main():
    data = read()[0]

    data_length = len(data)
    width = 25
    height = 6

    layer_length = width * height

    n_layers = data_length // layer_length
    final_image = ''

    for i in range(0, n_layers):
        start_index = layer_length * i
        end_index = start_index + layer_length
        sub_string = data[start_index:end_index]

        if i > 0:
            for j in range(0,layer_length):
                if final_image[j] == '2':
                    final_image = final_image[:j] + sub_string[j] + final_image[j + 1:]
        elif i == 0:
            final_image = sub_string

    print_image(final_image, width, height)

main()

