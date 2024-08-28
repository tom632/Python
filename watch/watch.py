import re
import sys


def main():
    print(parse(input("Enter HTML: ")))


def parse(s):
    if islink := re.search(r"<iframe src=\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"></iframe>", s):
        return f"https://youtu.be/{islink.group(2)}"
    else:
        return None


if __name__ == "__main__":
    main()
