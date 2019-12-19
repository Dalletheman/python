def readdata():
    with open('final.txt') as f:
        data = f.read().splitlines()
    return data


# dict is structured like this
# Example 9 ORE => 2 A will be Key = A; Val = 2,[ORE,9]
# Example 7 A, 1 E => 1 FUEL will be Key = FUEL; Val = 1,[[A, 7],[E, 1]]
def create_dict(data):
    dict = {}
    length = len(data)
    for i in range(0, length):
        ingredients_list = []
        reaction = data[i].split(' => ')
        ingredients = reaction[0].split(', ')

        for j in range(0, len(ingredients)):
            ingredient = ingredients[j].split(' ')
            ingredients_list.append([ingredient[1], int(ingredient[0])])

        product = reaction[1].split(' ')
        n_product = int(product[0])
        product_item = product[1]

        dict[product_item] = [n_product, ingredients_list]
    return dict

def calc_ore(dict):
    fuel = dict['FUEL']
    rest = {}
    ore_tot = [0]
    def calc_ore_inner(reaction, product, n_prev):

        length = len(reaction[1])
        n_product = reaction[0]
        multiple = 1
        if n_prev < n_product:
            rest_val = n_product - n_prev
            if product in rest:
                rest[product] = rest[product] + rest_val
            else:
                rest[product] = rest_val

        elif n_prev > n_product:
            if n_prev % n_product == 0:
                multiple = n_prev / n_product

            else:
                multiple = (n_prev // n_product) + 1
                rest_val = n_product * multiple - n_prev
                if product in rest:
                    rest[product] += rest_val
                else:
                    rest[product] = rest_val
        for i in range(0, length):
            next_product = reaction[1][i][0]








            # if there is rest of the item subtract the item value
            n_item = reaction[1][i][1] * multiple

            if next_product in rest:
                if n_item < rest[next_product]:
                    rest[next_product] -= n_item
                    n_item = 0
                else:
                    n_item -= rest[next_product]
                    rest[next_product] = 0

            if next_product == 'ORE':

                ore_tot[0] += n_item

            else:

                next_reaction = dict[next_product]
                n_current = n_item
                if n_current > 0:
                    calc_ore_inner(next_reaction, next_product, n_current)







    calc_ore_inner(fuel, 'FUEL', 1)
    return ore_tot



def main():
    data = readdata()


    dict = create_dict(data)

    ore_dict = calc_ore(dict)

    print(ore_dict)


main()