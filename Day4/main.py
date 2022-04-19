

def print_bingo(bingo):
    for bingo_line in bingo:
        print(bingo_line)

def check_horizontal(bingo):
    for bingo_line in bingo:
        is_bingo = True
        for bingo_number in bingo_line:
            if not bingo_number[0]:
                is_bingo = False
        if is_bingo:
            return True
    return False

def check_vertical(bingo):
    for j in range(len(bingo)):
        is_bingo = True
        for i in range(len(bingo)):
            if not bingo[i][j][0]:
                is_bingo = False
        if is_bingo:
            return True
    return False

def check_bingo(bingo):
    return check_horizontal(bingo) or check_vertical(bingo)

# return finished bingo if there is one. Otherwise return None
def check_for_first_finished_bingo(bingos):
    for bingo in bingos:
        if check_bingo(bingo):
            return bingo
    return None

# return last unfinished bingo if there is only one left. Otherwise return None
def check_for_last_finished_bingo(bingos):
    unfinished_bingos = []    
    for bingo in bingos:
        if not check_bingo(bingo):
            unfinished_bingos.append(bingo)
    if len(unfinished_bingos) == 1:
        return unfinished_bingos[0]
    else:
        return None
        
def calculate_result(input_number, finished_bingo):
    # calculate result
    # find sum of unmarked numbers on this board
    sum = 0
    for bingo_line in finished_bingo:
        for bingo_number in bingo_line:
            if not bingo_number[0]:
                sum += bingo_number[1]
    # multiply by the number that was just called
    last_number = input_number
    result = sum * last_number
    print("RESULT: {} * {} = {}".format(sum, last_number, result))


def main():
    input_file = "input.txt"
    with open(input_file) as file:
        # read lines
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

        input = lines[0].split(',')
        input = [int(x) for x in input]
        print(input)

        # remove first two lines
        lines.pop(0)
        lines.pop(0)

        bingos = []

        bingo = []
        # iterate lines
        for line in lines:
            if line:
                # append line to bingo
                line_list = line.split(' ')
                line_list = [int(x) for x in line_list if x]
                # add boolean to see if value was checked yet
                line_list = [(False, item) for item in line_list]

                bingo.append(line_list)
            else:
                # add finished bingo to bingos and reset bingo
                bingos.append(bingo)
                bingo = []
        
        # input was parsed, now play bingo

        last_finished_bingo = None
        for input_number in input:
            print(input_number)
            
            for bingo_idx, bingo in enumerate(bingos):
                for bingo_line_idx, bingo_line in enumerate(bingo):
                    for bingo_number_idx, bingo_number in enumerate(bingo_line):
                        if input_number == bingo_number[1]:
                            bingos[bingo_idx][bingo_line_idx][bingo_number_idx] = (True, bingo_number[1])
            
            ### STEP 1
            ### now check if a bingo was finished
            # first_finished_bingo = check_for_first_finished_bingo(bingos)
            # if finished_bingo is not None:
            #     print_bingo(finished_bingo)
            #     calculate_result(input_number, finished_bingo)
            #     return

            ### STEP 2
            if last_finished_bingo is not None and check_bingo(last_finished_bingo):
                # last finished bingo was just finished
                calculate_result(input_number, last_finished_bingo)
                return
            last_finished_bingo = check_for_last_finished_bingo(bingos)
            

if __name__ == "__main__":
    main()