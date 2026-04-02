num1 = int(input("Enter the first number: "))
print("choose which operator you want to use for calculating the numbers.")
operator = print("0. +", "1. -", "2. *", "3. /", "4. %", "5. //", "6. **")
print("Note: Enter numerics only base of the numbers assign to each operators...")
inpOP = int(input("Enter here: "))
num2 = int(input("Enter the second number: "))

if inpOP == 0:
    print(num1 + num2)
elif inpOP == 1:
    print(num1 - num2)
elif inpOP == 2:
    print(num1 * num2)
elif inpOP == 3:
    print(num1 / num2)
elif inpOP == 4:
    print(num1 % num2)
elif inpOP == 5:
    print(num1 // num2)
elif inpOP == 6:
    print(num1 ** num2)
else:
    print("Invalid input!!!")
    print("Please enter a valid number.")
