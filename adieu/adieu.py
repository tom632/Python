import inflect

name_list_join = inflect.engine()
name_list = []

while True:
    try:
        user_input = input("Name: ").strip().title()
        name_list.append(user_input)
    except EOFError:
        print()
        print("Adieu, adieu, to", name_list_join.join(name_list))
        break
