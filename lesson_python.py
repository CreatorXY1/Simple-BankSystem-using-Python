print("Hello, Python!" + "\n")
numbers_of_length = "Python is not hard at all but it is not easy either"
print(len(numbers_of_length))
print(numbers_of_length[12])
print(numbers_of_length[11:50])
print(numbers_of_length[-1])

# this section is using concatenated
print("what's up my niggas!" + "\n" + "Hello Madapaka!")
# this section is not used concatenated
print("what's up my niggas!" "\n" "Hello Madapaka!")
# this section does not use double quotation to separate texts
print("what's up my niggas!\nHello Madapaka!")

# this section is using escape character (meaning back slash(\))
test = "I'm gonna use 'back slash' symbol to separate strings\"see!?"
print(test)

# this is section teaching about formatted strings
first_name = "Inuzawa"
last_name = "Grimmoper"
# here in the full name, I'm using "white space" to get space between first name and last name
full_name = f"{first_name} {last_name}\n"
# but here, I'm not using "white space", so the result, the first name and last name are sticked to each other
full_name1 = f"{first_name}{last_name}"
integratedFN = full_name + full_name1
print(integratedFN)
# here, we use find method to get the index of the substring "per" in full_name1
print(full_name1.find("per"))
# here, we use replace method to replace the sequence of the assign characters
print(full_name.replace("Inuzawa", "Kurokawa"))
# here, I'm using operator "in" to search whether Inuzawa exist in the first_name I assign to the expression or not, if it exist, the result will be true, if it does not exist, the result will be false (which means it uses boolean value to express the result)
print("Inuzawa" in first_name)
print("Kurokawa" in first_name)
# here, I'm using operator "not in" to search whether Inuzawa exist in the first_name I assign to the expression or not, if it exist, the result will be false, if it does not exist, the result will be true (which means it uses boolean value to express the result)
print("Inuzawa" not in first_name)
print("Kurokawa" not in first_name)

# Addition
print(10 + 20)
# Subtraction
print(20 - 10)
# Multiplication
print(10 * 20)
# Division
print(20 / 10)
# Floor Division
print(20 // 10)
# Exponentiation
print(10 ** 2)
# Modulus
print(20 % 10)

# here, we can use normal assignment operator to assign value to x and y, and then we can use normal addition operator to add value to x and y
x = 100
y = 200
x = x + 100
y = y + 200
# here, we can also use augmented assignment operator to write the above code in a more concise way
x += 200
y += 400
# here, we can use the above code to get the integrated value of x and y
integratedXY = x + y
print(integratedXY)

# here, we can use the built-in function "round" to round the number to the nearest integer
print(round(22.9))
print(round(4.6))
# Note: Python uses "round half to even" for .5 ties: round(2.5) == 2, round(3.5) == 4
# Examples showing tie-to-even behavior
print(round(2.5))
print(round(3.5))
# here, we can use the built-in function "abs" to get the absolute value of a number
print(abs(-22.5))
print(abs(22.5))
print(abs(-10))
print(abs(10))
print(abs(11.5))
print(abs(-11.5))
print(abs(11))

# here, we can use the built-in function "type" to get the type of a variable or value
print(type(integratedXY))
print(type(first_name))

makyas = "Apple"
print(makyas[2:3])

# here, we can use conditional expression to write a simple if-else statement in a single line of code
rank = 1000
title1 = "Grandmaster"
titleF = "Bronze"

# here, we can use conditional expression to assign a value to the variable "message" based on the condition whether the rank is 100 or greater than 100 or not, if the condition is true, the value of message will be "Your rank is Grandmaster", if the condition is false, the value of message will be "Your rank is Bronze Sorry, for your rank..."
message = "Your rank is " + title1 if rank == 100 or rank >= 100 else "Your rank is " + \
    titleF + "\n" + "Sorry, for your rank..."
print(message)
# here, we can also use normal if-else statement to write the above code in a more traditional way
if rank == 100 or rank >= 100:
    print("Your rank is " + title1)
else:
    print("Your rank is " + titleF + "\n" + "Sorry, for your rank...")

not_student = False
student = True
credit_score = True
no_credit_score = False

# here, we can use logical operators "and" and "or" to combine multiple conditions in an if statement, if both conditions are true, the result will be true, if either condition is false, the result will be false
# conditions should be true for the if statement to execute the code block, if any of the conditions is false, the else block will be executed
if student and credit_score:
    print("You are a student with good credits")
else:
    print("Invalid input")
# here, we can use logical operator "not" to negate the condition in an if statement, if the condition is true, the result will be false, if the condition is false, the result will be true
# we use parentheses to group the conditions together, so that the "not" operator applies to the entire condition, if the condition is true, the result will be false, if the condition is false, the result will be true
if not (not_student and no_credit_score):
    print("You are not a student and you don't have good credits")
else:
    print("Invalid input")


for number in range(5):
    print("Yo!")
