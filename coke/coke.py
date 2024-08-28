price = 50
total_added = 0
money = [5, 10, 25]

while price > 0:
    print(f"Amount Due: {price}")
    inserted = int(input("Insert coin: "))
    if inserted in money:
        price = price - inserted
        total_added = total_added + inserted

if total_added >= price:
    print(f"Change Owed: {total_added - 50}")
