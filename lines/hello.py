# programme that will show the users input name and display each letter on a new row

user_input = input("Enter your name: ").strip()

for letters in user_input:
    print(letters)

print(f"Hello, {user_input}")
