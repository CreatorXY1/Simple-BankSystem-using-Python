# Checking Store Student Names


print("Check if your name is here in this database")

input_student_name = str(input("Enter the person name: "))


student_name = "Jeffrey", "Inuzawa", "John", "Anna", "Lilia", "Joana"

if input_student_name in student_name:
    print("The name you submit is stored here on database!")
    print("Name:", input_student_name)
elif input_student_name not in student_name:
    print("Sorry.. The name you entered is not in our database...")
    print("Please try other names later.")
else:
    print("Invalid name input!!!")
