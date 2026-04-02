num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your first number: "))
op = ("Choose which arithmethic you wanted to use: ")
print("1. +", "\t", "2. *", "\t", "3. -", "\t",
      "4. /", "\t", "5. %", "\t", "6. **")
select1 = int(input("Enter the number of the arithmetic you want to use: "))

sum = num1 + num2
multi = num1 * num2
sub = num1 - num2
modulo = num1 % num2
div = num1 / num2
expo = num1 ** num2

if select1 == 1:
    print("The sum of ", "num1", " + ", "num2 ", "= ", sum)
elif select1 == 2:
    print("The multiply of ", "num1", " x ", "num2 ", "= ", multi)
elif select1 == 3:
    print("The subtruction of ", "num1", " - ", "num2 ", "= ", sub)
elif select1 == 4:
    print("The division of ", "num1", " / ", "num2 ", "= ", div)
elif select1 == 5:
    print("The remainder of ", "num1", " % ", "num2 ", "= ", modulo)
elif select1 == 6:
    print("The exponentiation of ", "num1", " ** ", "num2 ", "= ", expo)
else:
    print("Invalid input!!!" /
          "Please input a valid number.")
