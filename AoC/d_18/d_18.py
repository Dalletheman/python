import math
import copy

def read():
    with open('input_4.txt') as f:
        data = f.read().splitlines()
    return data


def print_map(data):
    height = len(data)
    width = len(data[0])

    for i in range(0, height):
        for j in range(0, width):
            print(data[i][j], end='')
        print('')

def get_pos(data, char):
    length = len(data)
    for i in range(0, length):
        if char in data[i]:
            x = data[i].index(char)
            y = i
            break
    return [x,y]


def make_graph(data, start_pos):
    graph = {}
    graph['root'] = []

    def make_graph_inner(node, prev_pos, current_pos, route_length):
        y_change = -1
        x_change = 0

        next_positions = []

        for i in range(1,5):
            x_next = current_pos[0] + x_change
            y_next = current_pos[1] + y_change

            if not (x_next == prev_pos[0] and y_next == prev_pos[1]):
                next_val = data[y_next][x_next]
                if next_val == '.':
                    next_positions.append([x_next, y_next, '.'])
                elif next_val != '#':
                    next_positions.append([x_next, y_next, next_val])
            y_change_temp = y_change
            y_change = int(x_change*math.pow(-1, i))
            x_change = int(y_change_temp*math.pow(-1, i))

        # route_length > 0 since node should not be created when at root
        if len(next_positions) > 1 and route_length > 0:
            cord_string = '' + str(current_pos[0]) + str(current_pos[1])
            graph[node].append([cord_string, route_length])
            graph[cord_string] = []
            route_length = 0
            node = cord_string

        for i in range(0, len(next_positions)):
            x_next = next_positions[i][0]
            y_next = next_positions[i][1]
            next_val = next_positions[i][2]
            if next_val == '.':
                make_graph_inner(node, current_pos, [x_next, y_next], route_length + 1)
            elif next_val != '#':
                graph[node].append([next_val, route_length + 1])
                graph[next_val] = []
                make_graph_inner(next_val, current_pos, [x_next, y_next], 0)

    make_graph_inner('root', start_pos, start_pos, 0)

    return graph

def update_reachable_nodes(reachable_nodes, node_index):

    length_change = reachable_nodes[node_index][1]
    value = reachable_nodes[node_index][0]
    nr_nodes = len(reachable_nodes)
    remove_index = -1
    for i in range(0, nr_nodes):
        if value == reachable_nodes[i][0]:
            remove_index = i
        else:
            reachable_nodes[i][1] += length_change

    reachable_nodes.pop(remove_index)

def add_nodes(reachable_nodes, nodes):
    for i in range(0, len(nodes)):
        reachable_nodes.append(nodes[i])

def get_path_length(graph, tot_length, current_node):
    reachable_nodes = []
    keys = []
    path_lengths = []

    def gpl_inner(current_node, tot_length, reachable_nodes, keys):
        nodes = graph[current_node]
        add_nodes(reachable_nodes, nodes)
        if len(nodes) == 0 and len(reachable_nodes) == 0:
            path_lengths.append(tot_length)
        else:
            for i in range(0, len(reachable_nodes)):
                obj_value = reachable_nodes[i][0]
                length_change = reachable_nodes[i][1]
                if len(obj_value) > 1:
                    next_reachable_nodes = copy.deepcopy(reachable_nodes)
                    update_reachable_nodes(next_reachable_nodes, i)
                    gpl_inner(obj_value, tot_length + length_change, next_reachable_nodes, keys.copy())

                else:
                    if obj_value.isupper():
                        key = obj_value.lower()
                        if key in keys:
                            next_reachable_nodes = copy.deepcopy(reachable_nodes)
                            update_reachable_nodes(next_reachable_nodes, i)
                            gpl_inner(obj_value, tot_length + length_change, next_reachable_nodes, keys.copy())
                    else:
                        updated_keys = keys.copy()
                        updated_keys.append(obj_value)
                        next_reachable_nodes = copy.deepcopy(reachable_nodes)
                        update_reachable_nodes(next_reachable_nodes, i)
                        gpl_inner(obj_value, tot_length + length_change, next_reachable_nodes, updated_keys)

    gpl_inner(current_node, tot_length, reachable_nodes.copy(), keys.copy())

    return path_lengths

def main():
    data = read()
    print_map(data)

    start_pos = get_pos(data, '@')



    graph = make_graph(data, start_pos)
    print(graph)
    lengths = get_path_length(graph, 0, 'root')

    print(min(lengths))


    print(graph)





main()

