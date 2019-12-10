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
def calc_angle(main, check):
    x_main = main[0]
    y_main = main[1]
    x_check = check[0]
    y_check = check[1]

    if y_check > y_main:
        if x_check > x_main:
            angle = math.atan((y_check - y_main)/(x_check - x_main))*57.296
        elif x_check < x_main:
            angle = math.atan(abs(y_check - y_main) / abs(x_check - x_main)) * 57.296 + 270


    elif y_check < y_main:
        if x_check > x_main:
            angle = math.atan(abs(y_check - y_main) / abs(x_check - x_main)) * 57.296 + 90
        elif x_check < x_main:
            angle = math.atan((y_check - y_main) / (x_check - x_main)) * 57.296 + 180
    if y_check == y_main:
        if x_check > x_main:
            angle = 90
        elif x_check < x_main:
            angle = 270
    elif x_check == x_main:
        if y_check > y_main:
            angle = 0
        elif y_check < y_main:
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





main()