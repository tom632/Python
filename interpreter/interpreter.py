user_input = input("Expression: ").strip()
x, y, z = user_input.split(" ")

x = float(x)
z = float(z)

if y == "+":
    result = x + z
    print(f"{result: .1f}")
elif y == "-":
    result = x - z
    print(f"{result: .1f}")
elif y == "*":
    result = x * z
    print(f"{result: .1f}")
elif y == "/":
    result = x / z
    print(f"{result: .1f}")
