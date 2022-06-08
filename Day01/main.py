

input_file = "input.txt"

c1 = 0
c2 = 0
with open(input_file) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    for index in range(len(lines) - 1):
        prev1 = int(lines[index])
        curr1 = int(lines[index + 1])
        if prev1 < curr1:
            c1 = c1 + 1
    
    for index in range(len(lines) - 3):
        first = int(lines[index])
        second = int(lines[index + 1])
        third = int(lines[index + 2])
        fourth = int(lines[index + 3])

        prev2 = first + second + third
        curr2 = second + third + fourth
        if prev2 < curr2:
            c2 = c2 + 1


print("c1 = {}".format(c1))
print("c2 = {}".format(c2))