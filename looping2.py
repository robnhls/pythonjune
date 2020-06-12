
total = 0
count = 1
while True:  #when the test condition is too complicated for a single rule
    user_price = input(f"What is the price of item #{count} (q to quit) ")
    if user_price.lower() == "q":
        break # get out of the loop

    price = float(user_price)
    if price == 0:
        continue # go back to the beginning of the loop

    total += price
    count += 1

print(f"For your {count} items the price will be ${total:.2f}")
