

user_answer = input("Gimme a number: ") # 17

number = int(user_answer)


MIN_NUMBER = 25 # SHOUT_CAPS mean constant, do not change this value


is_big_enough = number > MIN_NUMBER

if is_big_enough:
    message = f"your number is {number} and the min is {MIN_NUMBER}"
    print(message)
else:
    print("that is too small")





