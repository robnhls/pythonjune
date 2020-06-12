

title = "Scope is fun"  # global variable
counter = 11


def printbook():

    global counter  # trust me. It will be fine
    title = "Are you there .... ?"  # creates a local  variable
    counter = counter + 1  # this will be global beause of the delcaration above
    print("Counter", counter)
    print("Book title", title)


print("normal", title)

# execute the printbook function
printbook()
printbook()
printbook()


print("normal again", title)
