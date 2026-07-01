import random

print("=====NUMBER GUESSING GAME=====")
print("YOU have to guess a number between 1 to 10")

guess_number = random.randint(1,10)  # Secret number made ONCE

while True:
    guess_any_number = int(input("Guess a number from 1 to 10: "))
    
    if guess_any_number == guess_number:
        print("Spot on, congratulations 🎉")
        break  # Win = exit game
    elif guess_any_number > guess_number:
        print("Sorry that is too high 😅")
    else:  # If not equal and not higher, must be lower
        print("Sorry that is too low 😂")

print("Welcome, anytime 😊")