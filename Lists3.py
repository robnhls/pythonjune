

names = ["Izzy","Jeff","Jim","Joan","Katie",
    "Leon","Mark", "Nirmita","Shakti", "Tim"]



# index = 0
# for name in names:
#     print(f"{index + 1} {name}")
#     index += 1


for index, name in enumerate(names):
    print(f"{index + 1} {name}")

while True:
    new_name = input("Name to add to the list: (-) to quit")

    if new_name == "-":
        break

    if new_name in names:
        print("We already have that name")
    else:
        names.append(new_name)
        names.sort()
        print("Added")

print(names)