
zip_codes = {"48111", "48162", "52123", "90812", "43210",
             "48111", "48162", "52123", "90812", "43210"}

# how many items in the set?
count = len(zip_codes)
print(count)

zip_codes.add("00123")

for zip in zip_codes:
    print(zip)


sales_person_a = {"48111", "48112", "48162"}

diff = sales_person_a.difference(zip_codes)

print(diff)
