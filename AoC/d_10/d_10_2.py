import math
def readdata():
    with open('final_input.txt') as f:
        data = f.read().splitlines()
    return data


def calc_coordinates(data):
    height = len(data)
    width = len(data[0])

    coordinates = []

    for i in range(0,height):
        for j in range(0,width):
            if data[i][j] == '#':
                cord = [j,i]
                coordinates.append(cord)

    return coordinates
#check angle between main asteroid and check asteroid
# 0,0 is at top left corner
def calc_angle(main, check):
    x_main = main[0]
    y_main = main[1]
    x_check = check[0]
    y_check = check[1]

    if y_check > y_main:
        if x_check > x_main:
            angle = math.atan((y_check - y_main)/(x_check - x_main))*57.296 + 90
        elif x_check < x_main:
            angle = math.atan(abs(x_check - x_main)/abs(y_check - y_main)) * 57.296 + 180


    elif y_check < y_main:
        if x_check > x_main:
            angle = math.atan(abs(x_check - x_main)/abs(y_check - y_main)) * 57.296
        elif x_check < x_main:
            angle = math.atan((y_check - y_main) / (x_check - x_main)) * 57.296 + 270
    if y_check == y_main:
        if x_check > x_main:
            angle = 90
        elif x_check < x_main:
            angle = 270
    elif x_check == x_main:
        if y_check < y_main:
            angle = 0
        elif y_check > y_main:
            angle = 180

    return angle



def number_detected(coordinates, index):

    x_main = coordinates[index][0]
    y_main = coordinates[index][1]

    #list of angles from main asteroid to others
    angles = []
    count = 0
    for i in range(0,len(coordinates)):
        if i != index:
            x_check = coordinates[i][0]
            y_check = coordinates[i][1]

            angle = calc_angle([x_main,y_main],[x_check, y_check])

            if angle not in angles:
                angles.append(angle)
                count += 1

    return count
def sort_coordinates(coordinates, index):
    x_main = coordinates[index][0]
    y_main = coordinates[index][1]
    # the structure of the sorted list is like:
    # elements in sorted list [[[angle],[distance],[coordinates]]]
    #sorted by angle and the elements inside the lists is sorted by distance
    sorted_list = []

    for i in range(0,len(coordinates)):
        if i != index:
            x_check = coordinates[i][0]
            y_check = coordinates[i][1]

            angle = calc_angle([x_main, y_main],[x_check, y_check])
            dist = pow(abs(x_main - x_check),2) + pow(abs(y_main - y_check),2)

            coordinate_struct = [angle, [x_check, y_check], dist]

            sort_list_length = len(sorted_list)
            for j in range(0, sort_list_length):
                angle_check = sorted_list[j][0][0]
                if angle == angle_check:
                    #insert struct into sorted list
                    sub_list_length = len(sorted_list[j])

                    for k in range(0,sub_list_length):
                        sub_list_dist = sorted_list[j][k][2]
                        if dist < sub_list_dist:
                            sorted_list[j].insert(k, coordinate_struct)
                            break
                        if k == sub_list_length and dist > sub_list_dist:
                            sorted_list[j].append(coordinate_struct)
                    break

                elif angle < angle_check:
                    sorted_list.insert(j, [coordinate_struct])
                    break
                elif angle > angle_check and j == sort_list_length - 1:
                    sorted_list.append([coordinate_struct])

            if sort_list_length == 0:
                sorted_list.append([coordinate_struct])

    return sorted_list




def main():
    data = readdata()
    coordinates = calc_coordinates(data)

    #run through all cordinates
    max_asteroids = 0
    best_coordinate = []
    for i in range(0, len(coordinates)):
        n = number_detected(coordinates, i)
        if n > max_asteroids:
            max_asteroids = n
            x_cord = coordinates[i][0]
            y_cord = coordinates[i][1]

            best_coordinate = [x_cord, y_cord]

    print("Best is: " + str(best_coordinate[0]) + ',' + str(best_coordinate[1]) + " with " + str(max_asteroids) + " asteroids detected")

    best_index = coordinates.index(best_coordinate)

    sorted_coordinates = sort_coordinates(coordinates, best_index)

    x = sorted_coordinates[199][0][1][0]
    y = sorted_coordinates[199][0][1][1]
    sum = x*100 + y


    print(x)
    print(y)
    print(sum)









main()