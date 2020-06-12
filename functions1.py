

def getpets():
    pets = []
    with open("pets.txt", "r") as file_input:
        for line in file_input:
            name = line.strip().lower()
            pets.append(name)
    return pets  # This will exit the function (kinda like break in a loop)


def printlist(lst, *headers, eol="", **footers):
    for header in headers:
        print(header)

    # only print a line if there are headers passed in
    if len(headers) > 0:
        print("-----------------")

    # print the actual list
    for item in lst:
        print(item + eol)

    if len(footers) > 0:
        print("-----------------")

    for name, value in footers.items():
        print(name, value)

    print()  # blank line


our_pets = getpets()

footers = {
    "author": "rob foulkrod",
    "copyright": 2020
}
printlist(our_pets, "Our Pets", "6/10/2020", author="rob foulkrod",
          course="Python Essentials", copyright=2020)


printlist(our_pets, "Our Pets", "6/10/2020", **footers)
