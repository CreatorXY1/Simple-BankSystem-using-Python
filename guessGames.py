# Guess Game!

import random


while True:

    print("Guess the number between 1 to 10")

    guessNum = random.randint(1, 10)

    attempt = 5

    while attempt > 0:
        user = int(input("Enter your number: "))

        if user > guessNum:
            print("Your number is higher!", "You guess it wrong, try again.")
        elif user < guessNum:
            print("Your number is lower!", "You guess it wrong, try again.")
        elif user == guessNum:
            print("You guess the number!")
            print("The number is: ", guessNum)
            print("Congratrulations!!!")
            print("Your score is: ", attempt)
            break
        else:
            print("Invalid input!!!")
            print("Please enter a valid number and try again.")

        attempt -= 1
        print("You only have ", attempt, " attempts left.")

        if attempt == 0:
            print("The correct number is ", guessNum)
            print("Game Over")
            print("Your score is: ", attempt)

    print("Play or Quit?")
    replay = str(input("").lower())

    option1 = str("Play")
    option2 = str("Quit")

    if replay == option1.lower():
        print("Your game will restart now!")
        print("Please wait a minute")
        print("We're preparing your game now...")
    elif replay == option2.lower():
        print("Thanks for playing this game :)")
        print("Good bye!")
        break
    else:
        print("Invalid input!!!")
        print('Please enter "Play" or "Quit" keywords only to avoid receiving error.')
        break