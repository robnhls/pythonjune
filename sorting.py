
numbers = (56, 3, 85, 12, 25, 69, 13, 46)

ordered = sorted(numbers, reverse=True)
print(ordered)

my_dictionary = {
    "b": 1,
    "a": 12,
    "d": 55,
    "c": 100,
    "e": 2
}

ordered = sorted(my_dictionary.items())
print(ordered)
new_dictionary = dict(ordered)
print(new_dictionary)

# print a dictionary in order
keys = sorted(my_dictionary.keys())

for key in keys:
    print(my_dictionary[key])


def lettercount(word):
    return len(word)


def lowercased(word):
    return word.lower()


def count_then_caseinsensitive(word):
    return len(word), word.lower()


emotions = ["joy", "rage", "confusion", "Confusion",
            "silly", "Relief", "happy", "sad", "odd"]
ordered = sorted(emotions, key=count_then_caseinsensitive)
print(ordered)

# same as above with wth lambdas this time
# optional, don't sweat it
ordered = sorted(emotions, key=lambda word: len(word))  # lettercount function
ordered = sorted(emotions, key=lambda emotion: emotion.lower()
                 )  # lowercased function
ordered = sorted(emotions, key=lambda e: (
    len(e), e.lower()))  # lowercased function
