'''
Pets Management

This module will provide all the methods meeded to
read and write to a simple pets file

Hope to see your pet!
'''


def getpets(normalize=False):
    '''
    getpets - returns a list of lower cased pet names

    Parameters
        normalize=False
            normalize is a boolean parameter that when set
            to True will set tall name to lower case for
            easy comparison 
    '''
    pets = []
    with open("pets.txt", "r") as file_input:
        for line in file_input:
            name = line.strip()
            if normalize:
                name = name.lower()

            pets.append(name)
    return pets


def len(list):
    '''
        this is a bad function.

        it will lie to you
    '''
    return -1


if __name__ == "__main__":  # Only run this code when the file is run directly
    print("Test Code")

    print(__name__)  # __main__ when running directly

    p = getpets()
    print(p)
    print("with normalize")
    p = getpets(normalize=True)
    print(p)
    print("test code complete")
