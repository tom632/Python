def main():
    user_input = input("Input: ").strip()
    shorten_string = shorten(user_input)
    print(f"Output: {shorten_string}")


def shorten(text):
    vowels = ["a", "e", "i", "o", "u"]
    removed = []
    for c in text:
        if c.casefold() not in vowels:
            removed.append(c)
    output = str("".join(removed))
    return output


if __name__ == "__main__":
    main()
