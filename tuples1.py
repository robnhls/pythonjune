
list_of_stuff = ["rob", "foulkrod", "detroit", "instructor", 48]
person1 = ("rob", "foulkrod", "detroit", "instructor", 48)
person2 = ("mark", "stevens", "palmer lake", "student", 48)
person3 = ("joan", "gonzalez", "framingham", "working on it", 50)
person4 = ("tim", "brown", "cleveland", "it manager", 54)
person5 = ("katie", "quinlivan", "worcester", "n/a", 29)
# we do not NEED () for tuples
person6 = "leon", "skillings", "hebron", "semi-retired", 65

# person1 = ("robert", "foulkrod", "detroit", "instructor", 48)

age = person1[age= 4]

list_of_stuff[0] = "Robert"
print(list_of_stuff)

# tuples cannot change, just build new ones
# person1[0] = "Robert" # immutable, cannot change

# print(person1)

people = [person1, person2, person3, person4, person5, person6]

# for loop
for person in people:
    fname, _, city, _, _ = person  # tuple is unpacked into variables

    print(f"{fname} is from {city}.")
