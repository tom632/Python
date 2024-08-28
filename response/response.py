import validators


def main():
    print(validate(input("Enter you email address: ")))


def validate(address):
    if validators.email(address) == True:
        return f"Valid"
    else:
        return f"Invalid"


if __name__ == "__main__":
    main()
