def main():
    user_input = calculate_fraction("Fraction: ")
    print(user_input)


def calculate_fraction(user_input):
    while True:
        try:
            x, y = input(user_input).split("/")
            if 0 <= int(x)/int(y) <= 0.1:
                return ("E")
            elif 0.9 <= int(x)/int(y) <= 1:
                return ("F")
            elif 0.1 < int(x)/int(y) < 0.9:
                return str(round(int(x)/int(y)*100)) + "%"
        except (ValueError, ZeroDivisionError):
            pass


main()
