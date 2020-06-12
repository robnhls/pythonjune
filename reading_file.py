
with open("pets.txt", "r") as pets_file:
    for line in pets_file:
        print(line.strip())

