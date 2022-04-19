


input_file = "input.txt"
with open(input_file) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    gamma = 0
    epsilon = 0

    str_length = len(lines[0])
    print("str_length = {}".format(str_length))
    count_ones_list = [0] * str_length
    count_zeros_list = [0] * str_length

    for line in lines:
        for index, char in enumerate(reversed(line)):
            bit = int(char)
            if bit:
                count_ones_list[index] = count_ones_list[index] + 1
            else:
                count_zeros_list[index] = count_zeros_list[index] + 1

    for index in range(str_length):
        if count_ones_list[index] > count_zeros_list[index]:
            gamma = gamma + (1 << index)
        elif count_ones_list[index] < count_zeros_list[index]:
            epsilon = epsilon + (1 << index)
        else:
            print("das nicht so nice")
    print(count_ones_list)
    print(count_zeros_list)

    print("gamma = {}".format(gamma))
    print("epsilon = {}".format(epsilon))

    result = gamma * epsilon
    print("result = {}".format(result))


    # part 2
    print("---------------- PART TWO ----------------")
    oxy_lines = list(lines)
    for index in range(str_length):
        count_one = 0
        count_zero = 0
        if len(oxy_lines) == 1:
            break

        for oxy_line in oxy_lines:
            if int(oxy_line[index]):
                count_one = count_one + 1
            else:
                count_zero = count_zero + 1
        
        most_common_bit = count_one >= count_zero
        oxy_lines = [oxy_line for oxy_line in oxy_lines if bool(int(oxy_line[index])) == most_common_bit]
        

    print(oxy_lines)

    co2_lines = list(lines)
    for index in range(str_length):
        count_one = 0
        count_zero = 0
        if len(co2_lines) == 1:
            break

        for co2_line in co2_lines:
            if int(co2_line[index]):
                count_zero = count_zero + 1
            else:
                count_one = count_one + 1
        
        most_common_bit = count_one > count_zero
        co2_lines = [co2_line for co2_line in co2_lines if bool(int(co2_line[index])) == most_common_bit]

    print(co2_lines)

    oxygen_generator_rating = int(oxy_lines[0], 2)
    co2_scrubber_rating = int(co2_lines[0], 2)
    print(oxygen_generator_rating)
    print(co2_scrubber_rating)
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    print(life_support_rating)
