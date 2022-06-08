### example main.py
from collections import deque
from functools import reduce

def point_is_lower_than_coordinates(point, heightmap, i, j):
    if i < 0 or i >= len(heightmap) or j < 0 or j >= len(heightmap[i]):
        return True
    else:
        return point < heightmap[i][j]

def is_lowest_point(heightmap, i, j):
    point = heightmap[i][j]

    return point_is_lower_than_coordinates(point, heightmap, i+1, j) and point_is_lower_than_coordinates(point, heightmap, i-1, j) and point_is_lower_than_coordinates(point, heightmap, i, j+1) and point_is_lower_than_coordinates(point, heightmap, i, j-1)

def is_not_yet_in_basin(heightmap, queue, i, j):
    # check if bounds are valid
    if i < 0 or i >= len(heightmap) or j < 0 or j >= len(heightmap[i]):
        return False
    # check if already in queue
    if (i, j) in queue:
        return False
    point = heightmap[i][j]
    return point != 9 and point != -1

def discover_basin(heightmap, i, j):
    basin = []
    queue = deque()
    queue.append((i,j))

    # while queue is not empty
    while(queue):
        (i,j) = queue.popleft()
        basin.append((i,j))
        # set this point to -1 so that it will not be added to queue again
        heightmap[i][j] = -1

        # check adjacent locations
        if is_not_yet_in_basin(heightmap, queue, i+1, j):
            queue.append((i+1,j))
        if is_not_yet_in_basin(heightmap, queue, i-1, j):
            queue.append((i-1,j))
        if is_not_yet_in_basin(heightmap, queue, i, j+1):
            queue.append((i,j+1))
        if is_not_yet_in_basin(heightmap, queue, i, j-1):
            queue.append((i,j-1))
    
    return basin

def find_basins(heightmap, lowest_points_coordinates):
    basins = []
    for (i, j) in lowest_points_coordinates:
        basins.append(discover_basin(heightmap, i, j))
            
    return basins

def get_product_of_n_largest_list_sizes(list_of_lists, n):
    list_lengths = [len(sublist) for sublist in list_of_lists]
    list_lengths.sort(reverse=True)
    # get n largest lengths of sublists
    top_n_list_lengths = list_lengths[0:n]

    # multiply all elements of list
    return reduce(lambda x, y : x*y, top_n_list_lengths)

def main():
    input_file = "input.txt"
    with open(input_file) as file:
        # read lines
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

        heightmap = []
        # iterate lines
        for line in lines:
            heightmap.append(list(map(int, list(line))))
        
        lowest_points_coordinates = []
        lowest_points = []
        for i in range(len(heightmap)):
            for j in range(len(heightmap[i])):
                if is_lowest_point(heightmap, i, j):
                    lowest_points.append(heightmap[i][j])
                    lowest_points_coordinates.append((i,j))
        
        risk_levels = [risk_level + 1 for risk_level in list(lowest_points)]
        # print(sum(lowest_points) + len(lowest_points))
        print(sum(risk_levels))

        basins = find_basins(heightmap, lowest_points_coordinates)

        n = 3
        result = get_product_of_n_largest_list_sizes(basins, n)
        print(result)


if __name__ == "__main__":
    main()