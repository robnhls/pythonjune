from collections import defaultdict


def one():
    return 1

def na(): 
    return "n/a"


counter_dictionary = defaultdict(one)
counter_dictionary["a"] = 15
counter_dictionary["b"] = 25

print(counter_dictionary["a"])
print(counter_dictionary["c"])
print(len(counter_dictionary))



regular = {}
regular.setdefault("a", 1)
print(regular["b"])