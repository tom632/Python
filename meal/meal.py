def main():
    user_input = input("What time is it? ").strip()

    time = convert(user_input)

    if 7.0 <= time <= 8.0:
        print("Breakfast time")
    if 12.0 <= time <= 13.0:
        print("Lunch time")
    if 18.0 <= time <= 19.0:
        print("Dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) * 1 / 60

    return float(hours+minutes)


if __name__ == "__main__":
    main()
