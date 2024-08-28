user_input = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

list = ["42", "forty two", "forty-two"]

if user_input in list:
    print("Yes")
else:
    print("No")
