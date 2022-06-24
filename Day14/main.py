from collections import Counter, defaultdict
import math
import operator

def read_input(lines):
    template = lines[0]
    rules = []
    for line in lines[2:]:
        rules.append(tuple(line.split(" -> ")))
    return template, dict(rules)

def convert_polymer(polymer):
    pair_occurences = []
    for i in range(len(polymer) - 1):
        pair_occurences.append(polymer[i] + polymer[i+1])
    pair_occurences = defaultdict(int, Counter(pair_occurences))
    return pair_occurences

def build_next_polymer(pair_occurences, rules):
    new_pair_occurences = defaultdict(int)
    for pair, quantity in pair_occurences.items():
        new_atom = rules[pair]
        new_pair_occurences[pair[0] + new_atom] += quantity
        new_pair_occurences[new_atom + pair[1]] += quantity
    return new_pair_occurences

def count_occurences(pair_occurences):
    char_occurences = defaultdict(int)
    for pair, quantity in pair_occurences.items():
        char_occurences[pair[0]] += quantity
        char_occurences[pair[1]] += quantity
    # divide all quantities by 2 and round up, since we are counting them twice
    # this will also correctly count the ones at the front and end
    char_occurences = {k: math.ceil(v / 2) for k, v in char_occurences.items()}
    char_occurences = dict(sorted(char_occurences.items(), key=lambda item: item[1], reverse=True))
    # occurence_list = list(char_occurences)
    # print(occurence_list)
    most_common = max(char_occurences.items(), key=operator.itemgetter(1))
    least_common = min(char_occurences.items(), key=operator.itemgetter(1))
    difference = most_common[1] - least_common[1]
    return char_occurences, most_common, least_common, difference

def main():
    input_file = "input.txt"
    with open(input_file) as file:
        # read lines
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        
        polymer, rules = read_input(lines)
        pair_occurences = convert_polymer(polymer)

        steps = 40
        for i in range(1, steps+1):
            pair_occurences = build_next_polymer(pair_occurences, rules)

        char_occurences, most_common, least_common, difference = count_occurences(pair_occurences)
        print(char_occurences)
        print(most_common)
        print(least_common)
        print(difference)


if __name__ == "__main__":
    main()