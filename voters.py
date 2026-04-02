# This is voters system

while True:

    validator = int(input("Enter your age: "))
    asking = print("Do you want to quit or continue?")
    user = str(input().lower())

    if user == "continue":

        if validator >= 24:
            print("You are eligible to vote presidential.")
        elif validator >= 18:
            print("You are eligible to vote sk only.")
        elif validator < 18:
            print("You are not eligible to vote. Thank you for trying to participate.")
        else:
            print("Invalid input!!!"
                  "Please try to input valid number.")
    elif user == "quit":
        print("Thank you for participating political voting, have a nice day!")
        break
    
