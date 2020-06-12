
# import petsmanagement as pm
from petsmanagement import getpets, len as count

pets = getpets()
count = count(pets)
print(pets, count)
