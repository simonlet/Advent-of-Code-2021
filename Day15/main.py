
import collections


### BFS SUCKS, USE DJIKSTRA INSTEAD! but i am too lazy now

def print_risk_levels(risk_levels):
    for rl in risk_levels:
        print(rl)

def coordinates_ok(risk_levels, x, y):
    return 0 <= y < len(risk_levels) and 0 <= x < len(risk_levels[y])

def main():
    input_file = "input.txt"
    with open(input_file) as file:
        # read lines
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        
        risk_levels = []
        for line in lines:
            risk_levels.append( [int(x) for x in line] )
        
        
        ### PART ONE
        start = (0,0)
        end = (len(risk_levels)-1, len(risk_levels[0])-1)

        paths = []
        queue = collections.deque([([start], 0)])
        while queue:
            path, path_risk = queue.popleft()
            x, y = path[-1]
            # if this path found the end, add it to paths
            if (x,y) == end:
                paths.append((path, path_risk))
            else:
                # for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                # only go right and down
                for x2, y2 in ((x+1,y), (x,y+1)):
                    if coordinates_ok(risk_levels, x2, y2) and (x2, y2) not in path:
                        queue.append((path + [(x2, y2)], path_risk + risk_levels[y2][x2]))

        print(len(paths))

        lowest_risk = min([path_risk for path,path_risk in paths])
        print(lowest_risk)

        print_risk_levels(risk_levels)



if __name__ == "__main__":
    main()