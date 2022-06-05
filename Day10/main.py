
def is_opening_char(char):
    opening_chars = ['(', '[', '<', '{']
    return char in opening_chars

def are_matching_brackets(opening_bracket, closing_bracket):
    return (opening_bracket == '(' and closing_bracket == ')') \
        or (opening_bracket == '[' and closing_bracket == ']') \
        or (opening_bracket == '{' and closing_bracket == '}') \
        or (opening_bracket == '<' and closing_bracket == '>')

def calculate_syntax_error_score(first_illegal_chars):
    score = 0
    for illegal_char in first_illegal_chars:
        if illegal_char == ')':
            score += 3
        elif illegal_char == ']':
            score += 57
        elif illegal_char == '}':
            score += 1197
        elif illegal_char == '>':
            score += 25137
        else:
            raise ValueError()
    return score

def calculate_line_completion_score(stack):
    bracket_score_dict = {
        '(' : 1,
        '[' : 2,
        '{' : 3,
        '<' : 4
    }
    score = 0
    for _ in range(len(stack)):
        char = stack.pop()
        
        score = score * 5 + bracket_score_dict[char]
    return score

def calculate_completion_score(stacks):
    scores = [calculate_line_completion_score(stack) for stack in stacks]
    scores.sort()

    middle_element = scores[len(scores)//2]
    return middle_element


def main():
    input_file = "input.txt"
    with open(input_file) as file:
        # read lines
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]


        first_illegal_chars = []
        stacks = []

        # iterate lines
        for line in lines:
            # split line into single characters
            line = list(line)
            
            stack = []

            illegal_char_found = False
            for char in line:
                # opening char -> append to stack
                if is_opening_char(char):
                    stack.append(char)
                # closing char -> check if equal to last opening char
                elif not are_matching_brackets(stack.pop(), char) and not illegal_char_found:
                    first_illegal_chars.append(char)
                    illegal_char_found = True
                    break
                # else do nothing since pop already deleted last entry of stack
            
            # discard corrupted lines and check if stack is not empty
            if not illegal_char_found and stack:
                stacks.append(stack)

        syntax_error_score = calculate_syntax_error_score(first_illegal_chars)
        print(syntax_error_score)

        completion_score = calculate_completion_score(stacks)
        print(completion_score)

        


if __name__ == "__main__":
    main()