import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import matplotlib
import numpy as np

def make_num_image(str_image, width):
    length = len(str_image)
    iterations = length // width

    int_map = np.zeros((1,25))

    for i in range(0,iterations):
        temp_array = np.array([0])
        start_index = width * i
        end_index = start_index + width
        sub_string = str_image[start_index:end_index]
        for j in range(0,width):
            number = int(sub_string[j])
            temp_array = np.append(temp_array, number)
        temp_array = temp_array[1:]
        int_map = np.vstack((int_map,temp_array))
    int_map = int_map[1:]
    return int_map
def reverse(num_image):
    int_map = np.zeros((1,25))

    for i in range(5,-1, -1):
        int_map = np.vstack((int_map,num_image[i]))
    int_map = int_map[1:]
    return int_map

string_image = "011001000110010011001001010010100011001010010100101000001010100101001011110100000010010010111101001010010001001001010010100100110000100011001001010010"





width = 25
num_image = make_num_image(string_image, width)
num_image = reverse(num_image)
print(num_image)
print(num_image[0][23])






cdict = {'red': ((0., 1, 1),
                 (0.05, 1, 1),
                 (0.11, 0, 0),
                 (0.66, 1, 1),
                 (0.89, 1, 1),
                 (1, 0.5, 0.5)),
         'green': ((0., 1, 1),
                   (0.05, 1, 1),
                   (0.11, 0, 0),
                   (0.375, 1, 1),
                   (0.64, 1, 1),
                   (0.91, 0, 0),
                   (1, 0, 0)),
         'blue': ((0., 1, 1),
                  (0.05, 1, 1),
                  (0.11, 1, 1),
                  (0.34, 1, 1),
                  (0.65, 0, 0),
                  (1, 0, 0))}

my_cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap',cdict,256)

pcolor(num_image,cmap=my_cmap)
colorbar()
show()