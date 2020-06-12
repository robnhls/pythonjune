
# show the contents of the file
with open("pets.txt", "r") as preview_file:
    whole_darn_thing = preview_file.read()
    print(whole_darn_thing)

print("------------------------------")


# Read into a list
pets = []
with open("pets.txt", "r") as file_input:
    for line in file_input:
        name = line.strip().lower()
        pets.append(name)
# auto close

# add many pets
while True:
    new_name = input("Enter pet name: (blank to quit) ")
    if new_name == "":
        break

    new_name = new_name.lower()
    if new_name in pets:
        print("WE have that name already")
    else:
        pets.append(new_name)
        print("added")


# save pets to disk
with open("pets.txt", "w") as file_output:
    pets.sort()
    for pet in pets:
        line = pet.title() + "\n"
        file_output.write(line)

print("File written")
