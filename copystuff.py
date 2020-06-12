from pprint import pprint


first_week = [["chicken", "marinade", "something else"],
              ["steak", "rice"],
              ["pizza"],
              ["braised short ribs", "roasted veg"],
              {"a": [11111111, 22222222, 33333333, 44444444, 5],
               "b":[1, 2, 3, 4, 5, [6, 7, 8, 9, 10]]}
              ]

second_week = first_week[:]

print("first_list", first_week)
pprint(first_week, depth=2)

# print("second_list", second_week)

# first_week.append("stir fry")

# print("first_list", first_week)
# print("second_list", second_week)
