
def main():
    input_file = "input.txt"
    with open(input_file) as file:
        # read lines
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

        # iterate lines
        for line in lines:
            pass

if __name__ == "__main__":
    main()