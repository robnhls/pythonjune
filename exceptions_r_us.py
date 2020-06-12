

file_name = input("Enter pets filename: ")


try:
    with open(file_name, "r") as pets_file:
        for name in pets_file:
            name = name.strip()
            print(name)
except:
    print(f"Cannot file filename {file_name}.")

