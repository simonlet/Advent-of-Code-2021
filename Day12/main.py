

def get_cave_connections(lines):
    cave_connections = []
    for line in lines:
        cave_connections.append(line.split('-'))
    return cave_connections

def get_all_caves(cave_connections):
    # get all caves
    caves = set()
    for connection in cave_connections:
        for cave in connection:
            caves.add(cave)
    return caves

def compute_possible_next_cave(cave_connections, cave):
    next_caves = []
    for connection in cave_connections:
        if cave in connection:
            if cave == connection[0]:
                # connection[1] is the connected cave
                next_caves.append(connection[1])
            else:
                # connection[0] is the connected cave
                next_caves.append(connection[0])
    return next_caves

def create_connection_dict(cave_connections):
    connection_dict = dict()
    caves = get_all_caves(cave_connections)
    for cave in caves:
        connection_dict[cave] = compute_possible_next_cave(cave_connections, cave)
    return connection_dict

def is_upper_case_string(string):
    return string == string.upper()

def get_possible_next_caves(path, connection_dict, current_cave, part_two):
    possible_next_caves = connection_dict[current_cave]
    # remove 'start' from possible next caves
    possible_next_caves = [cave for cave in possible_next_caves if cave != 'start']

    small_cave_count_dict = {cave : path.count(cave) for cave in path if not is_upper_case_string(cave) and cave != 'start'}
    small_cave_was_visited_twice = 2 in small_cave_count_dict.values()
    
    keep = []
    for next in possible_next_caves:
        cave_visits = path.count(next)
        # is big cave or was not yet visited
        if is_upper_case_string(next) or cave_visits == 0:
            keep.append(next)
        # is small cave and was visited already -> check if can be visited again and was visited only once
        elif part_two and not small_cave_was_visited_twice and cave_visits == 1:
            keep.append(next)

    possible_next_caves = keep
    return possible_next_caves


def main():
    input_file = "input.txt"
    with open(input_file) as file:
        # read lines
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        

        cave_connections = get_cave_connections(lines)

        #########################################
        ### PART ONE
        # part_two = False
        ### PART ONE
        part_two = True
        #########################################

        # brute force all possible combinations

        connection_dict = create_connection_dict(cave_connections)
        print(connection_dict)

        paths = [['start']]
        path_was_extended = True
        while path_was_extended:
            path_was_extended = False

            # put paths of next step here
            next_paths = []
            
            for path in paths:
                # get current position                
                current_cave = path[-1]
                # if current_cave is end, continue
                if current_cave == 'end':
                    next_paths.append(path)
                    continue
                # calculate where one could go to next
                possible_next_caves = get_possible_next_caves(path, connection_dict, current_cave, part_two)

                # if there are possible paths, add them to next_paths and set bool
                if possible_next_caves:
                    for next_cave in possible_next_caves:
                        next_paths.append(path + [next_cave])
                    path_was_extended = True
                else:
                    next_paths.append(path)

            paths = next_paths
        

        # remove paths that do not end at 'end'
        paths = [path for path in paths if path[-1] == 'end']

        # print("----------------------")
        # for path in paths:
        #     print(path)

        print(len(paths))
                

        

if __name__ == "__main__":
    main()