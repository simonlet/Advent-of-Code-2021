
from re import sub


def parse_input(lines):
    # iterate lines
    octopuses = []
    for line in lines:
        octopuses.append([int(o) for o in list(line)])
    return octopuses

def print_map(map):
    for sublist in map:
        print(sublist)

def apply_func_to_sublists_of_list(func, list):
    return [[func(x) for x in sublist] for sublist in list]


# check if index is in bounds and if flash map already flashed
def safe_index_increment(octopuses, flash_map, x, y):
    if y >= 0 and y < len(octopuses) and x >= 0 and x < len(octopuses[y]):
        if not flash_map[y][x]:
            octopuses[y][x] += 1 

def flash(octopuses, flash_map, x, y):
    # set current octopus timer to 0
    octopuses[y][x] = 0
    flash_map[y][x] = True
    # increment all octopus around the current octopus
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            safe_index_increment(octopuses, flash_map, x+i, y+j)
    

def main():
    input_file = "input.txt"
    with open(input_file) as file:
        # read lines
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        
        octopuses = parse_input(lines)

        flash_count = 0
        found_first_time_all_octopuses_flashed = False

        steps = 500
        for step_count in range(steps):
            octopuses = apply_func_to_sublists_of_list(lambda x : x+1, octopuses)

            # bitmap to check which octopuses already flashed
            flash_map = [[False for _ in range(len(octopuses[i]))] for i in range(len(octopuses))]

            # while something is changing, keep updating
            has_flashed = True
            while(has_flashed):
                has_flashed = False
                # check if octopuses flash
                for y in range(len(octopuses)):
                    for x in range(len(octopuses[y])):
                        if octopuses[y][x] > 9:
                            flash(octopuses, flash_map, x, y)
                            flash_count += 1
                            has_flashed = True
            
            ### PART TWO
            if not found_first_time_all_octopuses_flashed and sum(sum(octopuses, [])) == 0:
                print("Mashallah, alle Oktopusse haben gerade gleichzeitig geleuchtet:", step_count+1)
                found_first_time_all_octopuses_flashed = True
            
        # print octopuses
        print_map(octopuses)
        print_map(flash_map)

        print(flash_count)
        
                        
                    
if __name__ == "__main__":
    main()