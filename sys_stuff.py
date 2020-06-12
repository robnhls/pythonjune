import os

# os.system("pets.txt")  # fire and forget it

# not a great option when we want the output :(
# os.system("ipconfig")

with os.popen("ipconfig") as ip:
    for line in ip:
        if "IPv4" in line:
            # IPv4 Address. . . . . . . . . . . : 10.24.100.112
            address = line.split(":")[1].strip()

print(f"My IP address is {address}")
