
class Vent:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    def __repr__(self):
        return "({}, {} -> {}, {})".format(self.x1, self.y1, self.x2, self.y2)


def seperate_vents(vents):
    non_diagonal_vents = []
    diagonal_vents = []
    for vent in vents:
        if vent.x1 == vent.x2 or vent.y1 == vent.y2:
            non_diagonal_vents.append(vent)
        else:
            diagonal_vents.append(vent)
    return non_diagonal_vents, diagonal_vents

def main():
    input_file = "input.txt"
    with open(input_file) as file:
        # read lines
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

        vents = []
        # iterate lines
        for line in lines:
            line_split = line.split(" -> ")
            line_split1 = line_split[0].split(",")
            line_split2 = line_split[1].split(",")
            vent = Vent(x1=int(line_split1[0]), x2=int(line_split2[0]), y1=int(line_split1[1]), y2=int(line_split2[1]))
            vents.append(vent)
        
        # get max x and y value
        max_x = max(max(vent.x1 for vent in vents), max(vent.x2 for vent in vents)) + 1
        max_y = max(max(vent.y1 for vent in vents), max(vent.y2 for vent in vents)) + 1
        
        field = [[0] * max_y for _ in range(max_x)]

        # filter out diagonal vents
        non_diagonal_vents, diagonal_vents = seperate_vents(vents)
        print(len(vents))
        print(len(non_diagonal_vents))
        print(len(diagonal_vents))

        # STEP 1
        # now update the field for every non diagonal vent
        for vent in non_diagonal_vents:
            if vent.x1 == vent.x2:
                # iterate along y axis
                for y in range(min(vent.y1, vent.y2), max(vent.y1, vent.y2) + 1):
                    field[vent.x1][y] += 1
            elif vent.y1 == vent.y2:
                # iterate along x axis
                for x in range(min(vent.x1, vent.x2), max(vent.x1, vent.x2) + 1):
                    field[x][vent.y1] += 1
            else:
                print("Error! Diagonal vents should not be used here!")
                return
        
        # STEP 2
        for vent in diagonal_vents:
            # define step direction
            if vent.y1 < vent.y2:
                y_step = 1
            else:
                y_step = -1

            if vent.x1 < vent.x2:
                diagonal_min_x = vent.x1
                diagonal_max_x = vent.x2
                # start iterating at x1, this means, we need to start at y1
                y = vent.y1
            else:
                diagonal_min_x = vent.x2
                diagonal_max_x = vent.x1
                # start iterating at x1, this means, we need to start at y1
                y = vent.y2
                # in this case, we need to also negate the y step direction again
                y_step *= -1

            for x in range(diagonal_min_x, diagonal_max_x + 1):
                field[x][y] += 1
                y += y_step

        # count instances where there are 2 or more vents at the same point
        vent_overlap_count = 0
        for x in range(max_x):
            for y in range(max_y):
                if field[x][y] >= 2:
                    vent_overlap_count += 1
        
        print("RESULT: {} overlapped points".format(vent_overlap_count))




if __name__ == "__main__":
    main()