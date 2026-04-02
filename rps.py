# Rock, Paper, and Scissor Game!

import random

title1 = "GOAT"
title2 = "Predictor"
title3 = "Manipulator"
title4 = "Gambler"
title5 = "Unknown"

while True:
    count = 10
    p1score = 0
    p2score = 0
    print("Welcome to our Rock, Paper, and Scissor Game!\n".center(100))

    # I need to make ranking system that set a title for a player if the player continously getting score and holding highest score
    # But first, I need to figure it out how to save the score of a player that holds from inner while loop.
    # The goal is to find the right code on how to get the score from the inner while loop to save it from the outer while loop so that the score will continously adding up and get the higher chance for the players to get the best title's..

    print("Ranking System")

    if p1score == 0 and p2score == 0:
        print("Player 1")
        print("Rank: ", title5)
        print("Player 2")
        print("Rank: ", title5)
        print("No rank defined")
        print("Please start playing to get a title\n")
        print(p1score)
        print(p2score)
    elif p1score == 10 or p2score == 10:

        if p1score == 10:
            print("Player 1")
            print("Rank: ", title4)
        elif p2score == 10:
            print("Player 2")
            print("Rank: ", title4)
        else:
            print("Rank not defined to all players.")
    elif p1score == 20 or p2score == 20:

        if p1score == 20:
            print("Player 1")
            print("Rank: ", title3)
        elif p2score == 20:
            print("Player 2")
            print("Rank: ", title3)
        else:
            print("Rank not defined to all players.")
    elif p1score == 30 or p2score == 30:

        if p1score == 30:
            print("Player 1")
            print("Rank: ", title2)
        elif p2score == 30:
            print("Player 2")
            print("Rank: ", title2)
        else:
            print("Rank not defined to all players.")
    elif p1score == 40 or p2score == 40:

        if p1score == 40:
            print("Player 1")
            print("Rank: ", title1)
        elif p2score == 40:
            print("Player 2")
            print("Rank: ", title1)
        else:
            print("Rank not defined to all players.")
    else:
        print("No rank defined")
        print("Please start playing to get a title")
    
    while True:
        count -= 1

        print("Choose what you want to use for beating your opponent.")
        print("Rock, Paper or Scissor\n")
        print(
            "Note: Enter Rock, Paper, or Scissor keyword only to avoid receiving errors...\n")

        player1 = str(input("Enter here: ").lower())
        player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()

        if player1.lower() == player2.lower():
            print("Player 1 is ", player1, "Player 2 is ", player2)
            print("Tie")
            print("Player 1 score: ", p1score)
            print("Player 2 score: ", p2score)
        elif player1.lower() == "Rock".lower() and player2.lower() == "Scissor".lower():
            print("Player 1 is ", player1, "Player 2 is ", player2)
            print("Player 1 Win!")
            print("You Win!")
            p1score += 1
            print("Player 1 score: ", p1score)
            print("Player 2 score: ", p2score)
        elif player1.lower() == "Paper".lower() and player2.lower() == "Rock".lower():
            print("Player 1 is ", player1, "Player 2 is ", player2)
            print("Player 1 Win!")
            print("You Win!")
            p1score += 1
            print("Player 1 score: ", p1score)
            print("Player 2 score: ", p2score)
        elif player1.lower() == "Rock".lower() and player2.lower() == "Paper".lower():
            print("Player 1 is ", player1, "Player 2 is ", player2)
            print("Player 2 is Win!")
            print("You lose!")
            p2score += 1
            print("Player 1 score: ", p1score)
            print("Player 2 score: ", p2score)
        elif player1.lower() == "Scissor".lower() and player2.lower() == "Paper".lower():
            print("Player 1 is ", player1, "Player 2 is ", player2)
            print("Player 1 Win!")
            print("You Win!")
            p1score += 1
            print("Player 1 score: ", p1score)
            print("Player 2 score: ", p2score)
        elif player1.lower() == "Paper".lower() and player2.lower() == "Scissor".lower():
            print("Player 1 is ", player1, "Player 2 is ", player2)
            print("Player 2 is Win!")
            print("You lose!")
            p2score += 1
            print("Player 1 score: ", p1score)
            print("Player 2 score: ", p2score)
        elif player1.lower() == "Scissor".lower() and player2.lower() == "Rock".lower():
            print("Player 1 is ", player1, "Player 2 is ", player2)
            print("Player 2 is Win!")
            print("You lose!")
            p2score += 1
            print("Player 1 score: ", p1score)
            print("Player 2 score: ", p2score)
        else:
            print("Invalid input!!!")

        if count == 0:
            print("Game Over!")
            if p1score > p2score:
                print("Now, let's announce the winner of this game")
                print("The winner is...")
                print("Player 1!")
                print("Who got the highest score of: ", p1score)
                print("Congratulations for winning this game :D")
                print("We're proud of you :)")

                print("Player 2 be better next time")
                print("Don't give until you win :D")

                print("Thank you all for participating of this game")
                print("We hope you enjoy our joyful moment :D")
                print(
                    "We're gonna announce that we have another upcoming main game event this year so, be it guys!")
                print("We hope to see you again :)")
            elif p1score < p2score:
                print("Now, let's announce the winner of this game")
                print("The winner is...")
                print("Player 2!")
                print("Who got the highest score of: ", p2score)
                print("Congratulations for winning this game :D")
                print("We're proud of you :)")

                print("Player 1 be better next time")
                print("Don't give until you win :D")

                print(
                    "We're gonna announce that we have another upcoming main game event this year so, be it guys!")
                print("We hope to see you again :)")
            elif p1score == 0 and p2score == 0:
                print(
                    "Sorry for announcing this but, unfortunately, there is no winner of this game :(")
                print("Both players got ", p1score, " : ", p2score)

                print(
                    "Please get back stronger to get the top 1 highest score of this game")
                print("We're gonna settle this for now...")
                print("Thank you for you support")
                print("Players can play again by moving to the game restart section.")
            else:
                print("The winner of this game is...")
                print("Both of you!")
                print("Player 1 and Player 2")
                print("Who got score of ", p1score, " : ", p2score)
                print("Congratulations you two :D")
                print("You're doing very well, we're very proud of you :)")

                print(
                    "We're gonna announce that we have another upcoming main game event this year so, be it guys!")
                print("We hope to see you again :)")
            break

    if count == 0:
        print("Do you still want to play again or not?")
        decide = str(input("Enter your choice here: ").lower())

        if decide.lower() == "Play again".lower() or decide.lower() == "Play".lower():
            print("Okay!")
            print("Please let me prepare the game for you :)")
            print("Loading...")
        elif decide.lower() == "Not".lower() or decide.lower() == "No".lower() or decide.lower() == "Quit".lower():
            print("Are you sure?")
            decide = str(input("").lower())

            if decide.lower() == "Yes".lower() or decide.lower() == "Yep".lower():
                print("Thank you for playing with us :)")
                print("Have a nice day!")
                break
            elif decide.lower() == "No".lower():
                print("Then do you want to play again or not?")
                decide = str(input("").lower())

                if decide.lower() == "Yes".lower() or decide.lower() == "Play".lower():
                    print("Okay!")
                    print("Please let me prepare the game for you :)")
                    print("Loading...")
                elif decide.lower() == "No".lower() or decide.lower() == "Not".lower():
                    print("Thank you for playing with us :)")
                    print("Have a nice day!")
                    break
    else:
        print("Invalid input!!!")
        break
