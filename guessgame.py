import random

print("Number Guess Game!!!")

print("Guess the number between 1 to 10!")
guess1 = int(input("Enter your number here: "))

guess2 = random.randint(1, 10)

if guess2 == guess1:
    print("You guess the number!")
    print("The guess number is ", guess2)
    print("Congratulations!")
else:
    print("You didn't guess the number :(", "Try again.")
    print("The guess number is ", guess2)
