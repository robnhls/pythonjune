
names = ["Izzy","Jeff","Jim","Joan","Katie","Leon","Mark", "Nirmita","Shakti", "Tim"]


# names.append("Mark", "Tim")
# names.append("Tim")
names.extend(["Mark", "Tim"])

names.sort()

# say hi to everyone

for person in names:
    print(f"Hi, {person}")



notes = "ABCDEFG" # strings can be looped over, just like lists
for note in notes:
    print(note)

