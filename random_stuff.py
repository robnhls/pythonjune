import random


suits = ["H", "D", "C", "S"]
ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split()

cards = [(rank, suit) for rank in ranks for suit in suits]

print(random.choice(cards))
random.shuffle(cards)

for c in cards:
    print(c)
