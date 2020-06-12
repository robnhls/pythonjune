person1 = ("rob", "foulkrod", "detroit", "instructor", 48)
person2 = ("mark", "stevens", "palmer lake", "student", 48)
person3 = ("joan", "gonzalez", "framingham", "working on it", 50)
person4 = ("tim", "brown", "cleveland", "it manager", 54)
person5 = ("katie", "quinlivan", "worcester", "n/a", 29)
person6 = "leon", "skillings", "hebron", "semi-retired", 65

people = [person1, person2, person3, person4, person5, person6]


# print all the even aged folks with loops
# evens = []  # creating an empty list

# for person in people:
#     age = person[4]
#     if age % 2 == 0:
#         evens.append(person)

# get the even aged folks with a comprehension
evens = [
    p                 # select
    for p in people   # from
    if p[4] % 2 == 0     # where
]
print(evens)


print('start')
#  4 letter first names
four_letter_names = (
    firstname
    for firstname, _, _, _, _ in people
    if len(firstname) == 4
)

# or
#four_letter_names = [ p[0] for p in people if len(p[0]) == 4 ]


for name in four_letter_names:
    print(name)
