### example main.py
from collections import defaultdict

# add lanternfish to more smart data structure
def calculate_smart_lanternfish(lanternfish):
    smart_lanternfish = defaultdict(int)
    for lf in lanternfish:
        smart_lanternfish[lf] += 1
    return smart_lanternfish

def smart_populate_lf(lanternfish, days):
    lanternfish = calculate_smart_lanternfish(lanternfish)

    for _ in range(days):
        next_day_lanternfish = defaultdict(int)
        for lf_days_left, lf_amount in lanternfish.items():

            if lf_days_left == 0:
                # reset timer and add new lanternfish
                next_day_lanternfish[6] += lf_amount
                next_day_lanternfish[8] += lf_amount
            else:
                # move lf_amount down one
                next_day_lanternfish[lf_days_left-1] += lf_amount

        lanternfish = next_day_lanternfish

        print(lanternfish)
    
    print(sum(lanternfish.values()))
    return lanternfish


# naive answer for part 1
def populate_lf(lanternfish, days):
    for _ in range(days):
        new_lf_count = 0
        for i, lf in enumerate(lanternfish):
            if lf == 0:
                lanternfish[i] = 6
                new_lf_count += 1
            else:
                lanternfish[i] -= 1

        lanternfish.extend([8] * new_lf_count)

    print(len(lanternfish))


def main():
    input_file = "input.txt"
    with open(input_file) as file:
        # read lines
        line = file.readlines()[0]


        lanternfish = line.split(',')
        lanternfish = [int(l) for l in lanternfish]

        ##### PART ONE
        days = 80

        # populate_lf(lanternfish, days)
        # smart_populate_lf(lanternfish, days)


        ##### PART TWO
        days_part_two = 256
        smart_populate_lf(lanternfish, days_part_two)
        

        



if __name__ == "__main__":
    main()