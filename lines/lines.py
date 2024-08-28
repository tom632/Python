import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-3:] != ".py":
            sys.exit("Not a python file")
        else:
            print(count_lines(sys.argv[1]))


def count_lines(file):
    try:
        line_counter = 0
        with open(file, "r") as f:
            for lines in f:
                if not (lines.lstrip().startswith("#") or lines.strip() == ""):
                    line_counter = line_counter + 1
            return line_counter
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
