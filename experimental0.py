# This is a lab experiment for exploring different data types and user input in python.
import random

bread = 20.4
orange = 20.3
chicken = 100.23

qty_bread = float(input("How much bread you want to buy: "))
total_price = qty_bread * bread
qty_bread *= bread
print("Total price of bread is: ", total_price)
print("Total price of bread is: ", qty_bread)

qty_orange = float(input("How much orange you want to buy: "))
qty_orange *= orange
print("The total price of your orange is ", qty_orange)

qty_chicken = float(input("How much chicken kilo's you want: "))
qty_chicken *= chicken
print("The total price of chicken is ", qty_chicken)

print("Overall cost is", qty_bread + qty_orange + qty_chicken)


types_of_bread = ["0. Anadama bread", "1. Anpan",
                  "2. Appam", "3. Apple bread", "4. Arboud"]
price_of_breads = [27, 90, 22, 19, 33]
announcer = print("The types of bread we have are: ", "\n",
                  types_of_bread[0], "\t", types_of_bread[1], "\t", types_of_bread[2], "\t", types_of_bread[3], "\t", types_of_bread[4])
select = int(input("Enter the number of bread type you select: "))
if select == 0:
    print("The price of this bread is ", price_of_breads[0])
elif select == 1:
    print("The price of this bread is ", price_of_breads[1])
elif select == 2:
    print("The price of this bread is ", price_of_breads[2])
elif select == 3:
    print("The price of this bread is ", price_of_breads[3])
elif select == 4:
    print("The price of this bread is ", price_of_breads[4])
else:
    print("Invalid selection. Please select a number between 0 and 4.")

# This is a lab experiment for exploring different data types and user input in python.
testingINT = 33
testingSTR = "Hello madapaka!"
testingFLOAT = 332.32

print(f'This is an integer: {testingINT}')
print(f"This is a string: {testingSTR}")
print(f"This is a float: {testingFLOAT}")

# This is a packing and unpacking experiment in python.
fruit = ["banana", "Orange", "Mango"]
x, y, z = fruit

print(x)
print(y)
print(z)

# This is a random number generator experiment in python.
# The random module in python provides functions for generating random numbers. The randrange() function generates a random number within a specified range. In this case, it generates a random number between 1 and 100 (inclusive).
print(random.randrange(1, 100))