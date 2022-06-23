from math import dist
from operator import attrgetter, itemgetter


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self) -> str:
        return "({}, {})".format(self.x, self.y)

def read_input(lines):
    points = []
    folds = []

    done_reading_points = False
    for line in lines:
        if line:
            # line is not empty
            if not done_reading_points:
                # point
                point_split = line.split(',')
                points.append(Point(int(point_split[0]), int(point_split[1])))
            else:
                # fold
                fold_split = line.split(' ')[-1].split('=')
                folds.append((fold_split[0], int(fold_split[1])))
        else:
            # line is empty
            done_reading_points = True

    return points, folds

def set_points(paper, points):
    for point in points:
        paper[point.y][point.x] = 1

def print_paper(paper):
    print("-----------------")
    for line in paper:
        # print(*line, sep='\t')
        print(line)

def fold_paper(paper, points, fold):
    (axis, fold_line) = fold
    new_points = []
    for point in points:
        point_axis_coordinate = getattr(point, axis)
        if point_axis_coordinate > fold_line:
            # needs to be folded
            distance = point_axis_coordinate - fold_line
            if axis == 'x':
                # fold by x
                y = point.y
                x = point.x - 2*distance
            elif axis == 'y':
                # fold by y
                y = point.y - 2*distance
                x = point.x
            paper[y][x] = 1
            new_points.append(Point(x,y))
        else:
            # point does not need to be mirrored so can stay in next step
            new_points.append(point)
    # cut off paper at fold_line
    if axis == 'x':
        paper = [line[:fold_line] for line in paper]
    elif axis == 'y':
        paper = paper[:fold_line]

    return paper, new_points

def count_dots_on_paper(paper):
    return sum( [ row.count(1) for row in paper])

def main():
    input_file = "input.txt"
    with open(input_file) as file:
        # read lines
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        
        points, folds = read_input(lines)

        # print(points)
        # print(folds)

        x_max = max(points, key=attrgetter('x')).x + 1
        y_max = max(points, key=attrgetter('y')).y + 1

        # print(x_max, y_max)

        paper = [[0] * x_max for _ in range(y_max)]

        # set marked points on paper to True
        set_points(paper, points)

        # print_paper(paper)


        ### PART ONE
        part_one_paper, _ = fold_paper(paper, points, folds[0])
        print(count_dots_on_paper(part_one_paper))

        ### PART TWO
        for fold in folds:
            paper, points = fold_paper(paper, points, fold)
        print_paper(paper)



if __name__ == "__main__":
    main()