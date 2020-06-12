
user_count = input("How many items do you have? ")
count = int(user_count)

items_priced = 0
total = 0
while items_priced < count:
    user_item = input(f"what is the price of item #{items_priced + 1}? ")
    price = float(user_item)

    total += price
    items_priced += 1

print(f"for your {count} items the price will be ${total:.2f}")
