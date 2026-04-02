#  Task: Simple Dice Roller Game
# Here’s the challenge:
# The computer rolls two dice (numbers between 1 and 6). (check)
# The player rolls two dice as well. (check)
# Compare totals: (check)
# Higher total wins. (check)
# Same total = Tie. (check)
# Add a replay option so the player can keep rolling until they quit.
# (Optional) Add a score tracker for wins, losses, and ties.

import random as rd

playerName1 = "Player 1"
playerName2 = "Player 2"
result = "Tie"

while True:

    while True:
        print("\nReady Player1?")
        print("Enter 'Start' or 'Ready' if you want to play.")
        print("Enter 'Quit', if you want to fortfeit the game.")
        startingPointp1 = str(input("").lower())

        if startingPointp1.lower() == "Start".lower() or startingPointp1.lower() == "Ready".lower() or startingPointp1.lower() == "S".lower() or startingPointp1.lower() == "R".lower():
            print("Greate!")
            print("Now...")
            break
        elif startingPointp1.lower() == "No".lower():
            print("Okay")
            print("We're gonna wait until you're ready.")
            print("Just let us know if you're ready or wanna quit.")
            print(
                "Just enter your decision here so that we will now what decision you've made.")
            print("Note: If you want to quit just type 'Quit'")
            decisionp1 = str(input("").lower)

            if decisionp1.lower() == "Quit".lower():
                print("Okay!")
                print(
                    "If that's your decision then, thank you for participating this game player 1 :D")
                print(
                    "Just let us know if you want to participate again so that we can prepare the game for you :)")
                print("So, that's quit game then!")
                print("See you next time!")
                break
            elif decisionp1.lower() == "Start".lower() or decisionp1.lower() == "Ready".lower() or decisionp1.lower() == "S".lower() or decisionp1.lower() == "R".lower():
                print("Okay!")
                print("Let's ask Player 2 if he want's to play with you :D")
                break
            else:
                print("Invalid Input!!!")
        elif startingPointp1.lower() == "Quit".lower():
            print("Thank you for participating our game :)")
            print("We hope we see you again in this game for the next upcoming challenge")
            print("Good bye!")
            break
        else:
            print("Invalid Input!!!")

        if decisionp1.lower() == "Quit".lower():
            print("")
            break

    if (startingPointp1.lower() == "Start".lower() or startingPointp1.lower() == "Ready".lower() or startingPointp1.lower() == "S".lower() or startingPointp1.lower() == "R".lower()) or (decisionp1.lower() == "Start".lower() or decisionp1.lower() == "Ready".lower() or decisionp1.lower() == "S".lower() or decisionp1.lower() == "R".lower()):
        while True:
            print("\nReady Player2?")
            print("Enter 'Start' or 'Ready' if you want to play.")
            print("Enter 'Quit', if you want to fortfeit the game.")
            startingPointp2 = str(input("").lower())

            if startingPointp2.lower() == "Start".lower() or startingPointp2.lower() == "Ready".lower() or startingPointp2.lower() == "S".lower() or startingPointp2.lower() == "R".lower():
                print("Greate!")
                break
            elif startingPointp2.lower() == "No".lower():
                print("Okay")
                print("We're gonna wait until you're ready.")
                print("Just let us know if you're ready or wanna quit.")
                print(
                    "Just enter your decision here so that we will now what decision you've made.")
                print("Note: If you want to quit just type 'Quit'")
                decisionp2 = str(input("").lower)

                if decisionp2.lower() == "Quit".lower():
                    print("Okay!")
                    print(
                        "If that's your decision then, thank you for participating this game player 2 :D")
                    print(
                        "Just let us know if you want to participate again so that we can prepare the game for you :)")
                    print("So, that's quit game then!")
                    print("See you next time!")
                    break
                elif decisionp2.lower() == "Start".lower() or decisionp2.lower() == "Ready".lower() or decisionp2.lower() == "S".lower() or decisionp2.lower() == "R".lower():
                    print("Okay!")
                    print("Let's ask Player 2 if he want's to play with you :D")
                    break
                else:
                    print("Invalid Input!!!")
            elif startingPointp2.lower() == "Quit".lower():
                print("Thank you for participating our game :)")
                print(
                    "We hope we see you again in this game for the next upcoming challenge")
                print("Good bye!")
                break
            else:
                print("Invalid Input!!!")

            if decisionp2.lower() == "Quit".lower():
                print("")
                break

    if (startingPointp1.lower() == "Start".lower() or startingPointp1.lower() == "Ready".lower() or startingPointp1.lower() == "S".lower() or startingPointp1.lower() == "R".lower()) or (startingPointp2.lower() == "Start".lower() or startingPointp2.lower() == "Ready".lower() or startingPointp2.lower() == "S".lower() or startingPointp2.lower() == "R".lower()):

        print("Player's Dice's rolling...")
        diceOne = int(rd.randint(1, 6))
        dice1 = int(rd.randint(1, 6))

        diceTwo = int(rd.randint(1, 6))
        dice2 = int(rd.randint(1, 6))

        player1 = diceOne + dice1
        player2 = diceTwo + dice2

        if player1 > player2:
            print("\nThe winner is: ", playerName1,)
            print("Dice one: ", diceOne)
            print("Dice two: ", dice1)
            print("Total: ", player1, "\n")

            print(playerName2)
            print("Dice one: ", diceTwo)
            print("Dice two: ", dice2)
            print("Total: ", player2)
        elif player1 < player2:
            print("\nThe winner is: ", playerName2,)
            print("Dice one: ", diceTwo)
            print("Dice two: ", dice2)
            print("Total: ", player2, "\n")

            print(playerName1,)
            print("Dice one: ", diceOne)
            print("Dice two: ", dice1)
            print("Total: ", player1)
        elif player1 == player2:
            print(playerName1)
            print("Dice one: ", diceOne)
            print("Dice two: ", dice1)
            print("Total: ", player1, "\n")

            print(playerName2)
            print("Dice one: ", diceTwo)
            print("Dice two: ", dice2)
            print("Total: ", player2, "\n")

            print("Result: ", result)
        else:
            print("Invalid input!!!")
            break
    else:
        print("Invalid Input!!!")
        break
