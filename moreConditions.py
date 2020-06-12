
count = input("How many coffees do you need? ")
count = int(count)


plurality = "coffee" if count == 1 else "coffees" 

message = f"you will get {count} {plurality}"
print(message)
