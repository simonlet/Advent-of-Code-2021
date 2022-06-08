### example main.py
from collections import defaultdict
import math

def calculate_smart_crabs(crabs):
    smart_crabs = defaultdict(int)
    for lf in crabs:
        smart_crabs[lf] += 1
    return smart_crabs

# use this one for part one
def move_crabs_from_pos(num_crabs_at_pos, from_position, to_position):
    return num_crabs_at_pos * abs(from_position - to_position)

# use this one for part two
def move_crabs_from_pos2(num_crabs_at_pos, from_position, to_position):
    steps = abs(from_position - to_position)
    steps_cost = (steps * (steps + 1) / 2)
    return num_crabs_at_pos * steps_cost

def move_all_crabs(crabs, to_position):
    fuel_cost = 0
    for crab_position, num_crabs_at_pos in crabs.items():
        fuel_cost += move_crabs_from_pos2(num_crabs_at_pos, crab_position, to_position)
    return fuel_cost

def main():
    input_file = "input.txt"
    with open(input_file) as file:
        # read lines
        line = file.readlines()[0]


        crabs = [int(l) for l in line.split(',')]
        crabs = calculate_smart_crabs(crabs)
        # print(crabs)



        max_value = max(crabs.keys())
        print(max_value)

        results = dict()
        result_list = []
        for to_position in range(max_value + 1):
            # results[to_position] = move_all_crabs(crabs, to_position)
            result_list.append(move_all_crabs(crabs, to_position))
        
        print(result_list)
        print(min(result_list))
        print(result_list.index(min(result_list)))
        

if __name__ == "__main__":
    main()