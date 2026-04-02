class Bank:

    def __init__(self, fullname, age, birthdate, address, username, email, password):
        self.fullname = fullname
        self.age = age
        self.birthdate = birthdate
        self.address = address
        self.username = username
        self.email = email
        self.password = password

    def account(self):
        print("Account Profile")
        print("Full name:", self.fullname)
        print("Age:", self.age)
        print("Birth date:", self.birthdate)
        print("Address:", self.address)
        print("Username:", self.username)
        print("Email:", self.email)
        print("Password:", self.password)

    def accountLogin(self):

        while True:

            print("Login")

            userORemail = str(input("Enter your username/email: "))

            if userORemail == self.username or userORemail == self.email:

                while True:

                    userPass = str(input("Enter your pass: "))

                    if userPass == self.password:
                        print("Successfully Login!")

                        print("Welcome Back", self.username)
                        break
                    elif userPass != self.password:
                        print("Incorrect input password!!!")
                        print("Please enter correct password")
                    else:
                        print("Invalid input!!!")

                    if userPass == self.password:
                        break
                    else:
                        print("Please try again...")

            elif userORemail != self.username or userORemail != self.email:
                print("Wrong username or email input...")
                print("Please enter the correct username or email")

            else:
                print("Wrong Credentials!!!")

            if userORemail == self.username or userORemail == self.email:
                break


class BankStatement():

    def __init__(self, balance, deposit, withdraw):
        self.balance = balance
        self.deposit = deposit
        self.withdraw = withdraw

    def userBalance(self):
        print("Your balance:", self.balance)

    def userDeposit(self):

        while True:
            print("How much money you want to deposit?")

            user0 = int(input("Enter cash to deposit: "))

            if user0 == int(user0):
                sum = user0 + self.balance
                self.balance = sum

                print("Successfully deposit!")
                print("Your current balance now is: ", self.balance)

                print("Do you want to deposit again?")
                print("Enter (Y/n) or (Yes/No)")

                while True:
                    user1 = str(input("Enter here: ").lower())

                    if user1.lower() == "Yes".lower() or user1.lower() == "Y".lower():
                        break
                    elif user1.lower() == "No".lower() or user1.lower() == "N".lower():
                        break
                    else:
                        print("Invalid input!!!")
                        print("Please enter a valid credentials")
            else:
                print("Invalid input!!!")
                print("Please enter a correct input to avoid recieving errors...")

            if user1.lower() == "No".lower() or user1.lower() == "N".lower():
                break

    def userWithdraw(self):

        while True:
            print("How much money you want to withdraw?")

            user2 = int(input("Enter here: "))

            if user2 == int(user2):

                if self.balance < user2:

                    print("Sorry, you don't have enough balance to withdraw...")
                    print("Continue depositing for best withdraw services.")
                    break

                elif self.balance >= user2:
                    sub = self.balance - user2
                    self.balance = sub

                    print("Successfully withdraw!")
                    print("Your current balance now is: ", self.balance)

                    print("Do you want to withdraw again?")
                    print("Enter (Y/n) or (Yes/No)")

                    while True:
                        user3 = str(input("Enter here: ").lower())

                        if user3.lower() == "Yes".lower() or user3.lower() == "Y".lower():
                            break
                        elif user3.lower() == "No".lower() or user3.lower() == "N".lower():
                            break
                        else:
                            print("Invalid input!!!")
                            print("Please enter a valid credentials")
            else:
                print("Invalid input!!!")
                print("Please enter a correct input to avoid recieving errors...")

            if user3.lower() == "No".lower() or user3.lower() == "N".lower():
                break


output0 = Bank("Jeffrey L. Autentico", 22, "December 31, 2003",
               "76-A, Bucana, St. John Prk 12-B", "Inuzawa01", "inuzawa01@gmail.com", "09650761906")
output1 = BankStatement(0, 0, 0)

output0.accountLogin()

while True:
    if (output0.username == "Inuzawa01" or output0.email == "inuzawa01@gmail.com") and output0.password == output0.password:
        output1.userBalance()

        print("Deposit")
        print("Withdraw")

        while True:

            userChoice = str(input("Enter your choice: ").lower())

            if userChoice.lower() == "Deposit".lower():
                output1.userDeposit()
                break
            elif userChoice.lower() == "Withdraw".lower():
                output1.userWithdraw()
                break
            else:
                print("Invalid input!!!")
    else:
        print("Wrong credentials!!!")

    print("Exit?")
    print("Enter (Y/n) or (Yes/No)")

    while True:
        userDecide = str(input("Enter here: ").lower())

        if userDecide.lower() == "Yes".lower() or userDecide.lower() == "Y".lower():
            print("Thank you for using our bank system :)")
            print("Have a nice day!")
            break
        elif userDecide.lower() == "No".lower() or userDecide.lower() == "N".lower():
            print("Okay :D")
            print("Let me prepare your bank statement now.")
            print("Please wait...")
            break
        else:
            print("Invalid input!!!")
            print("Please enter a valid keyword to avoid receiving error.")

    if userDecide.lower() == "Yes".lower() or userDecide.lower() == "Y".lower():
        break
