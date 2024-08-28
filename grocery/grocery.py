grocery_list = {}

while True:
    try:
        item = input().upper().strip()
        if item not in grocery_list:
            grocery_list[item] = 1
        else:
            grocery_list[item] = grocery_list[item] + 1
    except EOFError:
        sorted_list = dict(sorted(list(grocery_list.items())))
        for item in sorted_list:
            print(sorted_list[item], item, sep=" ")
        break
    except KeyError:
        pass
