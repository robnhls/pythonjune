names = ["Izzy", "Jeff", "Jim", "Joan", "Katie", "Leon", "Nirmita", "Shakti"]

count = len(names) # 8
a_name = names[5] # Leon
# not_a_name = names[99] #IndexError

another_name = names[-4]

j_people = names[1:4] # Jeff, Jim, Joan
last_four = names[-4:] # "Katie", "Leon", "Nirmita", "Shakti"
first_four = names[:4] # "Izzy", "Jeff", "Jim", "Joan"
odd_people = names[1::2]
print("odd people", odd_people)


print(j_people)