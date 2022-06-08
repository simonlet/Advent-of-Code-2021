from collections import defaultdict
import itertools
import json

class Dieter:
    def __init__(self, signal_patterns, output_digits):
        self.signal_patterns = signal_patterns
        self.output_digits = output_digits
        self.wire_mapping = dict()

    def __repr__(self):
        return "[ {}, {} ]".format(self.signal_patterns, self.output_digits)

    @staticmethod
    def is_one(digit):
        return len(digit) == 2
    @staticmethod
    def is_four(digit):
        return len(digit) == 4
    @staticmethod
    def is_seven(digit):
        return len(digit) == 3
    @staticmethod
    def is_eight(digit):
        return len(digit) == 7

    def count_1s_4s_7s_8s(self):
        count = 0
        for digit in self.signal_patterns:
            if Dieter.is_one(digit) or Dieter.is_four(digit) or Dieter.is_seven(digit) or Dieter.is_eight(digit):
                count += 1
        return count

    def get_unique_digit(self, is_needed_digit_func):
        for digit in self.signal_patterns:
            if is_needed_digit_func(digit):
                return set(digit)
        return None

    def deduce_digits(self):
        # first search for the 1, and deduce from there
        one = self.get_unique_digit(self.is_one)
        four = self.get_unique_digit(self.is_four)
        seven = self.get_unique_digit(self.is_seven)
        eight = set("abcdefg")

        # subtract 1 from 7 to get 'a' mapping
        self.wire_mapping['a'] = next(iter(seven - one))

        # combine set of 4 and 7 to get the 9
        temp = set(four) | set(seven)
        nine = None
        for digit in self.signal_patterns:
            digit = set(digit)
            if temp.issubset(digit) and len(digit) == 6:
                nine = digit
                self.wire_mapping['g'] = next(iter(digit - temp))
                break
        
        # find the one by searching for digit of length 6 that is not 9 and has length 4 when
        # subtracting the 1
        for digit in self.signal_patterns:
            digit = set(digit)
            if len(digit) == 6 and digit != nine and len(digit - one) == 4:
                zero = digit
                self.wire_mapping['d'] = next(iter(eight - zero))
        
        # find the six by searching for digit of length 6 that is not 9 and not zero
        for digit in self.signal_patterns:
            digit = set(digit)
            if len(digit) == 6 and digit != nine and digit != zero:
                six = digit
                self.wire_mapping['c'] = next(iter(eight - six))
                self.wire_mapping['e'] = next(iter(six - nine))
        
        # find the 5 by subtracting 'e' from 6
        five = six - set(self.wire_mapping['e'])

        # create three by adding 7 and 'd' and 'g'
        three = (seven | {self.wire_mapping['d']}) | {self.wire_mapping['g']}
        self.wire_mapping['b'] = next(iter(nine - three))

        # get wire mapping of 'f' by removing 'c' from 1
        self.wire_mapping['f'] = next(iter(one - {self.wire_mapping['c']}))

        # get 2 by removing 'b' and 'f' from 8
        two = eight - {self.wire_mapping['b']} - {self.wire_mapping['f']}


        # sort dictionary by key and print
        self.wire_mapping = dict(sorted(self.wire_mapping.items()))
        print(self.wire_mapping)

        #### with the correct mapping we can now create the missing numbers
        digit_mapping = {
            frozenset(zero) : 0,
            frozenset(one) : 1,
            frozenset(two) : 2,
            frozenset(three) : 3,
            frozenset(four) : 4,
            frozenset(five) : 5,
            frozenset(six) : 6,
            frozenset(seven) : 7,
            frozenset(eight) : 8,
            frozenset(nine) : 9
        }

        # now iterate through output_digits and add them up
        sum = 0
        multiple = 1000
        for output_digit in self.output_digits:
            od = digit_mapping[frozenset(output_digit)]
            print(od)
            sum += od * multiple
            multiple /= 10

        #
        printable_dm = dict()
        for key, value in digit_mapping.items():
            printable_dm[''.join(sorted(list(key)))] = value
        print(json.dumps(printable_dm, indent=4))
        
        return sum
        


        





def main():
    input_file = "input.txt"
    with open(input_file) as file:
        # read lines
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

        dieters = []
        # iterate lines
        for line in lines:
            
            # split line at delimiter '|'
            line_split = line.split(' | ')

            signal_pattern = line_split[0].split(' ')
            output_digits = line_split[1].split(' ')

            dieter = Dieter(signal_pattern, output_digits)
            dieters.append(dieter)
        
        #### PART ONE
        sum = 0
        for dieter in dieters:
            sum += dieter.count_1s_4s_7s_8s()
        print(sum)

        ### PART TWO
        sum = 0
        for i in range(len(dieters)):
            sum += dieters[i].deduce_digits()
        print("The result of part 2 is: {}".format(sum))


if __name__ == "__main__":
    main()