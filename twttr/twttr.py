vowels = ["a", "e", "i", "o", "u"]

user_input = input("Input: ").strip()

for c in user_input:
    if c.casefold() not in vowels:
        print(c, end="")

print()
