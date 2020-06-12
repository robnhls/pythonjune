
abvs = {
    "MI": "Michigan",
    "OH": "Ohio",
    "MS": "Mississippi",
    "WA": "Washington",
    "TX": "Texas"
}

print(abvs["MI"])

if "NY" in abvs:
    print(abvs["NY"])
else:
    print("I do not yet know that state. Updates are coming.")

# alternate way of doing the same thing
answer = abvs.get("NY", "Not Found")
print(answer)

# adding a new item to the dictionary
abvs["NY"] = "New York"

# sooooo many loops

# 1) loop over the keys (default)
print("Keys ....")
for abv in abvs:
    print(abv)

print("---------------------")

# 2) loop over values
print("Values ....")
for state in abvs.values():
    print(state)

print("---------------------")

# 3) I want EVERYTHING!!!!
print("Keys AND Values")
for pair in abvs.items():
    print(pair)

print("Keys AND Values again")
for abv, state in abvs.items():
    print(abv + " = " + state)
