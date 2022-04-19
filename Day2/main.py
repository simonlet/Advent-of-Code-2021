

horizontal_pos = 0
depth = 0

input_file = "input.txt"
with open(input_file) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    for line in lines:
        line = line.split()
        
        command = line[0]
        step = int(line[1])

        if command == "forward":
            horizontal_pos = horizontal_pos + step
        elif command == "up":
            depth = depth - step
        elif command == "down":
            depth = depth + step


result1 = horizontal_pos * depth
print("result1 = {}".format(result1))


horizontal_pos = 0
depth = 0
aim = 0

with open(input_file) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    for line in lines:
        line = line.split()
        
        command = line[0]
        step = int(line[1])

        if command == "forward":
            horizontal_pos = horizontal_pos + step
            depth = depth + aim * step
        elif command == "up":
            aim = aim - step
        elif command == "down":
            aim = aim + step

result2 = horizontal_pos * depth
print("result2 = {}".format(result2))

    # for index in range(len(lines)):
