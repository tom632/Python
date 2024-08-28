from PIL import Image, ImageOps
import sys
import os


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        image_format = [".jpg", ".jpeg", ".png"]
        input = os.path.splitext(sys.argv[1])
        output = os.path.splitext(sys.argv[2])
        if output[1].lower() not in image_format:
            sys.exit("Invalid output")
        elif input[1].lower() != output[1].lower():
            sys.exit("Input and output have different extensions")
        else:
            change_photo(sys.argv[1], sys.argv[2])


def change_photo(input, output):
    try:
        tshirt = Image.open("shirt.png")
        with Image.open(input) as input:
            cropped = ImageOps.fit(input, tshirt.size)
            cropped.paste(tshirt, mask=tshirt)
            cropped.save(output)
    except FileNotFoundError:
        sys.exit(f"Input does not exist")


if __name__ == "__main__":
    main()
