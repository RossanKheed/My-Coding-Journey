# Guess a number between 1 to 10
print("=====NUMBER GUESSING GAME=====")
print("YOU have to guess a number between 1 to 10")
guess_number=4
guess_any_number=int(input ("Enter a number between 1 to 10:"))
if guess_any_number == 4:
    print("Spot on ! . Congratulations 🎊 ")
elif guess_any_number >=5:
    print("It is too high 🤣 ")
else:
    print("It is too low 😂 ")