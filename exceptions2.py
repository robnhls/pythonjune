

while True:

    try:
        print("Open a fake thing")  # every time
        user_number = input("Gimme a number: ")  # 3.4 / non-number
        number = int(user_number)  # ValueError
        base = 100
        answer = base / number  # ZeroDivisionError
        print(f"Your answer is {answer}")
    except ValueError:
        print(f"'{user_number}' is not a whole number.")
    except ZeroDivisionError:
        print("Please do not enter 0. It hurts.")
    except Exception as err:  # This must be last
        print("You are awesome. We did not even think of that as a possibility.")
        # log the unknown exception (logging tomorrow)
    else:
        break
    finally:
        print("close a fake thing")  # every time

print(user_number)
