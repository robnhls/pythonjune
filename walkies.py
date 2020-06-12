
import os

base_path = "c:/py3master"

# dirpath and firnames should probably be _ instead because I'm not using them
for dirpath, dirnames, filenames in os.walk(base_path):
    for filename in filenames:
        if ".py" in filename:
            print(filename)
