# Calculator

while True:

    while True:
        print("Scientific Calculator")

        print("Please enter numbers only for calculating numericals...")

        num1 = int(input("Enter first number: "))
        print("+ ", "-")
        print("* ", "/")
        print("// ", "% ", "**")
        operators1 = str(input(
            "Choose one operator and enter the operator you've choose: "))
        num2 = int(input("Enter second number: "))

        operators2 = str(f"{"+"} {"-"} {"*"} {"/"} {"//"} {"%"} {"**"}")

        if operators1 == "+":
            print(num1 + num2)
            break
        elif operators1 == "-":
            print(num1 - num2)
            break
        elif operators1 == "*":
            print(num1 * num2)
            break
        elif operators1 == "/":
            print(num1 / num2)
            break
        elif operators1 == "//":
            print(num1 // num2)
            break
        elif operators1 == "%":
            print(num1 % num2)
            break
        elif operators1 == "**":
            print(num1 ** num2)
            break
        else:
            print("Invalid input!!!")
            print("Plase follow and read carefully the instruction given on the above.")

    print("Do you want to quit or not?")
    decision = str(input("")).lower()

    quit = "Quit".lower()
    noT = "Not".lower()
    no = "No".lower()

    if decision == quit.lower():
        print("Thank you for using us :D")
        print("Have a nice day!")
        break
    elif decision == noT.lower() or decision == no:
        print("Okay!")
        print("Let us prepare the calculator for you :)")
        print("Just wait a little bit...")
    else:
        print("Invalid input!!!")
        print("Please enter a valid keywords to avoid receiving errors...")
        break
