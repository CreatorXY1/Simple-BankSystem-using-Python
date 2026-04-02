class Bank:

    def __init__(self, card):
        self.card = card

    def cardType(self, type):
        self.type = type

    def account(self, name, id):
        self.name = name
        self.id = id


class BankAccount(Bank):

    def __init__(self, card, type, name, id, balance):
        super().__init__(card)
        super().cardType(type)
        super().account(name, id)
        self.balance = balance

    def result(self):
        print("BANK")
        print("Card type:", self.type)
        print("Account name:", self.name)
        print("Card ID:", self.id)
        print("Balance:", self.balance)


outputV0 = BankAccount("Credit", "Visa", "Inuzawa", 20220797, 500000)
outputV1 = BankAccount("Credit", "Visa", "Jeffrey", 12345678, 0)
outputM0 = BankAccount("Credit", "MasterCard", "Inuzawa", 12955509, 1000000)
outputM1 = BankAccount("Credit", "MasterCard", "Jeffrey", 98765432, 0)


class Product:

    def products(self, productName, productID):
        self.productName = productName
        self.productID = productID

    def productType(self, productBrand):
        self.productBrand = productBrand


class x1(Product):

    def __init__(self, productName, productID, productPrice):
        super().products(productName, productID)
        self.productPrice = productPrice

    def result(self):
        print("Product:", self.productName)
        print("ID:", self.productID)
        print("Price:", self.productPrice)


output1 = Product()
output1.productType("Smart Phone")
output1.productType("PC")

output2 = x1("Realme GT", 202290, 12902.22)
output3 = x1("Redmajic 12 Pro", 102203, 69999.99)
output4 = x1("ROG 9", 909233, 59999.23)

output5 = x1("Asus", 380023, 86000.0)
output6 = x1("Redmajic(PC version)", 787722, 92990.55)
output7 = x1("ROG(PC version)", 303320, 95999.99)

while True:
    print("Welcome to TrustNest Shop!")

    print("Please choose the following product type you want before proceeding to products")

    print("Smart Phone", "\n", "PC")
    while True:
        user = str(input("").lower())

        if user.lower() == "Smart Phone".lower():
            print("Which phone you like?\n")

            print(output2.productName)
            print(output3.productName)
            print(output4.productName)

            while True:
                select = str(input("").lower())

                if select.lower() == "Realme GT".lower():
                    output2.result()

                    print("Do you want to buy this sir?")

                    while True:
                        decision = str(input("").lower())

                        if decision.lower() == "Yes".lower():
                            print("Please enter your bank account")
                            print("We support Visa and MasterCard")
                            print(
                                "Please enter the following type of card you wanted to use :)")

                            while True:
                                ba = str(input("").lower())

                                if ba.lower() == outputV0.type.lower():

                                    while True:
                                        cardName = str(
                                            input("Enter your name: "))

                                        if cardName == outputV0.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputV0.id:
                                                    outputV0.result()
                                                    print(
                                                        "You have a balance of: ", outputV0.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output2.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputV0.balance > output2.productPrice:
                                                                
                                                                deducted = outputV0.balance - output2.productPrice

                                                                print("Balance:", outputV0.balance, "-", "Product price:",
                                                                      output2.productPrice, " =", (deducted))

                                                                print(
                                                                    "Your total balance now is:", outputV0.balance)

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputV0.balance < output2.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                            break
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputV0.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputV0.id:
                                                    break

                                        elif cardName == outputV1.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputV1.id:
                                                    outputV1.result()
                                                    print(
                                                        "You have a balance of: ", outputV1.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output2.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputV1.balance > output2.productPrice:

                                                                print("Balance:", outputV1.balance, "-", "Product price:",
                                                                      output2.productPrice, " =", (outputV1.balance - output2.productPrice))

                                                                print(
                                                                    "Your total balance now is:")
                                                                outputV1.result()

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputV1.balance < output2.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                            break
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputV1.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputV1.id:
                                                    break

                                        elif cardName != outputV1.name:
                                            print(
                                                "The name you input was not found")
                                            print(
                                                "Please enter a valid name again to avoid receiving error.")

                                        if cardName == outputV1.name:
                                            break
                                        elif cardName == outputV0.name:
                                            break

                                elif ba.lower() == outputM0.type.lower():

                                    while True:
                                        cardName = str(
                                            input("Enter your name: "))

                                        if cardName == outputM0.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputM0.id:
                                                    outputM0.result()
                                                    print(
                                                        "You have a balance of: ", outputM0.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output2.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputM0.balance > output2.productPrice:

                                                                print("Balance:", outputM0.balance, "-", "Product price:",
                                                                      output2.productPrice, " =", (outputM0.balance - output2.productPrice))

                                                                print(
                                                                    "Your total balance now is:")
                                                                outputM0.result()

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputM0.balance < output2.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputM0.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputM0.id:
                                                    break

                                        elif cardName == outputM1.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputM1.id:
                                                    outputM1.result()
                                                    print(
                                                        "You have a balance of: ", outputM1.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output2.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputM1.balance > output2.productPrice:

                                                                print("Balance:", outputM1.balance, "-", "Product price:",
                                                                      output2.productPrice, " =", (outputM1.balance - output2.productPrice))

                                                                print(
                                                                    "Your total balance now is:")
                                                                outputM1.result()

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputM1.balance < output2.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputM1.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputM1.id:
                                                    break

                                        elif cardName != outputM1.name:
                                            print(
                                                "The name you input was not found")
                                            print(
                                                "Please enter a valid name again to avoid receiving error.")
                                        else:
                                            print("Invalid input!!!")

                                        if cardName == outputM0.name:
                                            break
                                        elif cardName == outputM1.name:
                                            break

                                else:
                                    print("Invalid input 101!!!")
                                    print(
                                        "Please enter a valid card type to avoid receiving error.")

                                if ba.lower() == outputV0.type.lower():
                                    break
                                elif ba.lower() == outputM0.type.lower():
                                    break

                        elif decision.lower() == "No".lower():
                            print("Okay")
                            print(
                                "Comeback if you already decide to buy this item sir!")
                            break
                        else:
                            print("Invalid input 404!!!")
                            print(
                                "Please enter a valid answer to avoid receiving error.")

                        if decision.lower() == "Yes".lower():
                            break
                        elif decision.lower() == "No".lower():
                            break

                elif select.lower() == "Redmajic 12 Pro".lower():
                    output3.result()

                    print("Do you want to buy this sir?")

                    while True:
                        decision = str(input("").lower())

                        if decision.lower() == "Yes".lower():
                            print("Please enter your bank account")
                            print("We support Visa and MasterCard")
                            print(
                                "Please enter the following type of card you wanted to use :)")

                            while True:
                                ba = str(input("").lower())

                                if ba.lower() == outputV0.type.lower():

                                    while True:
                                        cardName = str(
                                            input("Enter your name: "))

                                        if cardName == outputV0.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputV0.id:
                                                    outputV0.result()
                                                    print(
                                                        "You have a balance of: ", outputV0.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output3.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputV0.balance > output3.productPrice:

                                                                print("Balance:", outputV0.balance, "-", "Product price:",
                                                                      output3.productPrice, " =", (outputV0.balance - output3.productPrice))

                                                                print(
                                                                    "Your total balance now is:")
                                                                outputV0.balance

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputV0.balance < output3.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                            break
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputV0.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputV0.id:
                                                    break

                                        elif cardName == outputV1.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputV1.id:
                                                    outputV1.result()
                                                    print(
                                                        "You have a balance of: ", outputV1.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output3.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputV1.balance > output3.productPrice:

                                                                print("Balance:", outputV1.balance, "-", "Product price:",
                                                                      output3.productPrice, " =", (outputV1.balance - output3.productPrice))

                                                                print(
                                                                    "Your total balance now is:")
                                                                outputV1.result()

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputV1.balance < output3.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                            break
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputV1.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputV1.id:
                                                    break

                                        elif cardName != outputV1.name:
                                            print(
                                                "The name you input was not found")
                                            print(
                                                "Please enter a valid name again to avoid receiving error.")

                                        if cardName == outputV1.name:
                                            break
                                        elif cardName == outputV0.name:
                                            break

                                elif ba.lower() == outputM0.type.lower():

                                    while True:
                                        cardName = str(
                                            input("Enter your name: "))

                                        if cardName == outputM0.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputM0.id:
                                                    outputM0.result()
                                                    print(
                                                        "You have a balance of: ", outputM0.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output3.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputM0.balance > output3.productPrice:

                                                                print("Balance:", outputM0.balance, "-", "Product price:",
                                                                      output3.productPrice, " =", (outputM0.balance - output3.productPrice))

                                                                print(
                                                                    "Your total balance now is:")
                                                                outputM0.result()

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputM0.balance < output3.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputM0.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputM0.id:
                                                    break

                                        elif cardName == outputM1.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputM1.id:
                                                    outputM1.result()
                                                    print(
                                                        "You have a balance of: ", outputM1.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output3.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputM1.balance > output3.productPrice:

                                                                print("Balance:", outputM1.balance, "-", "Product price:",
                                                                      output3.productPrice, " =", (outputM1.balance - output3.productPrice))

                                                                print(
                                                                    "Your total balance now is:")
                                                                outputM1.result()

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputM1.balance < output3.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputM1.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputM1.id:
                                                    break

                                        elif cardName != outputM1.name:
                                            print(
                                                "The name you input was not found")
                                            print(
                                                "Please enter a valid name again to avoid receiving error.")

                                        else:
                                            print("Invalid input!!!")

                                        if cardName == outputM1.name:
                                            break
                                        elif cardName == outputM0.name:
                                            break
                                else:
                                    print("Invalid input 101!!!")
                                    print(
                                        "Please enter a valid card type to avoid receiving error.")

                                if ba.lower() == outputV0.type.lower():
                                    break
                                elif ba.lower() == outputM0.type.lower():
                                    break

                        elif decision.lower() == "No".lower():
                            print("Okay")
                            print(
                                "Comeback if you already decide to buy this item sir!")
                            break
                        else:
                            print("Invalid input 404!!!")
                            print(
                                "Please enter a valid answer to avoid receiving error.")

                        if decision.lower() == "Yes".lower():
                            break
                        elif decision.lower() == "No".lower():
                            break
                elif select.lower() == "ROG 9".lower():
                    output4.result()

                    print("Do you want to buy this sir?")

                    while True:
                        decision = str(input("").lower())

                        if decision.lower() == "Yes".lower():
                            print("Please enter your bank account")
                            print("We support Visa and MasterCard")
                            print(
                                "Please enter the following type of card you wanted to use :)")

                            while True:
                                ba = str(input("").lower())

                                if ba.lower() == outputV0.type.lower():

                                    while True:
                                        cardName = str(
                                            input("Enter your name: "))

                                        if cardName == outputV0.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputV0.id:
                                                    outputV0.result()
                                                    print(
                                                        "You have a balance of: ", outputV0.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output4.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputV0.balance > output4.productPrice:

                                                                print("Balance:", outputV0.balance, "-", "Product price:",
                                                                      output4.productPrice, " =", (outputV0.balance - output4.productPrice))

                                                                print(
                                                                    "Your total balance now is:")
                                                                outputV0.balance

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputV0.balance < output4.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                            break
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputV0.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputV0.id:
                                                    break

                                        elif cardName == outputV1.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputV1.id:
                                                    outputV1.result()
                                                    print(
                                                        "You have a balance of: ", outputV1.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output4.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputV1.balance > output4.productPrice:

                                                                print("Balance:", outputV1.balance, "-", "Product price:",
                                                                      output4.productPrice, " =", (outputV1.balance - output4.productPrice))

                                                                print(
                                                                    "Your total balance now is:")
                                                                outputV1.result()

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputV1.balance < output4.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                            break
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputV1.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputV1.id:
                                                    break

                                        elif cardName != outputV1.name:
                                            print(
                                                "The name you input was not found")
                                            print(
                                                "Please enter a valid name again to avoid receiving error.")

                                        if cardName == outputV0.name:
                                            break
                                        elif cardName == outputV1.name:
                                            break

                                elif ba.lower() == outputM0.type.lower():

                                    while True:
                                        cardName = str(
                                            input("Enter your name: "))

                                        if cardName == outputM0.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputM0.id:
                                                    outputM0.result()
                                                    print(
                                                        "You have a balance of: ", outputM0.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output4.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputM0.balance > output4.productPrice:

                                                                print("Balance:", outputM0.balance, "-", "Product price:",
                                                                      output4.productPrice, " =", (outputM0.balance - output4.productPrice))

                                                                print(
                                                                    "Your total balance now is:")
                                                                outputM0.result()

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputM0.balance < output4.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputM0.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputM0.id:
                                                    break

                                        elif cardName == outputM1.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputM1.id:
                                                    outputM1.result()
                                                    print(
                                                        "You have a balance of: ", outputM1.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output4.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputM1.balance > output4.productPrice:

                                                                print("Balance:", outputM1.balance, "-", "Product price:",
                                                                      output4.productPrice, " =", (outputM1.balance - output4.productPrice))

                                                                print(
                                                                    "Your total balance now is:")
                                                                outputM1.result()

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputM1.balance < output4.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputM1.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputM1.id:
                                                    break

                                        elif cardName != outputM1.name:
                                            print(
                                                "The name you input was not found")
                                            print(
                                                "Please enter a valid name again to avoid receiving error.")

                                        else:
                                            print("Invalid input!!!")

                                        if cardName == outputM0.name:
                                            break
                                        elif cardName == outputM1.name:
                                            break

                                else:
                                    print("Invalid input 101!!!")
                                    print(
                                        "Please enter a valid card type to avoid receiving error.")

                                if ba.lower() == outputV0.type.lower():
                                    break
                                elif ba.lower() == outputM0.type.lower():
                                    break

                        elif decision.lower() == "No".lower():
                            print("Okay")
                            print(
                                "Comeback if you already decide to buy this item sir!")
                            break
                        else:
                            print("Invalid input 404!!!")
                            print(
                                "Please enter a valid answer to avoid receiving error.")

                        if decision.lower() == "Yes".lower():
                            break
                        elif decision.lower() == "No".lower():
                            break
                else:
                    print("Invalid input 101!!!")
                    print("Please enter a valid phone to avoid receiving error.")

                if select.lower() == "Realme GT".lower():
                    break
                elif select.lower() == "ROG 9".lower():
                    break
                elif select.lower() == "Redmajic 12 Pro".lower():
                    break

        elif user.lower() == "PC".lower():
            print("Which PC you like?")

            print(output5.productName)
            print(output6.productName)
            print(output7.productName)

            while True:
                select = str(input("").lower())

                if select.lower() == "Asus".lower():
                    output5.result()

                    print("Do you want to buy this sir?")

                    while True:
                        decision = str(input("").lower())

                        if decision.lower() == "Yes".lower():
                            print("Please enter your bank account")
                            print("We support Visa and MasterCard")
                            print(
                                "Please enter the following type of card you wanted to use :)")

                            while True:
                                ba = str(input("").lower())

                                if ba.lower() == outputV0.type.lower():

                                    while True:
                                        cardName = str(
                                            input("Enter your name: "))

                                        if cardName == outputV0.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputV0.id:
                                                    outputV0.result()
                                                    print(
                                                        "You have a balance of: ", outputV0.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output5.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputV0.balance > output5.productPrice:

                                                                print("Balance:", outputV0.balance, "-", "Product price:",
                                                                      output5.productPrice, " =", (outputV0.balance - output5.productPrice))

                                                                print(
                                                                    "Your total balance now is:")
                                                                outputV0.balance

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputV0.balance < output5.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                            break
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputV0.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputV0.id:
                                                    break

                                        elif cardName == outputV1.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputV1.id:
                                                    outputV1.result()
                                                    print(
                                                        "You have a balance of: ", outputV1.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output5.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputV1.balance > output5.productPrice:

                                                                print("Balance:", outputV1.balance, "-", "Product price:",
                                                                      output5.productPrice, " =", (outputV1.balance - output5.productPrice))

                                                                print(
                                                                    "Your total balance now is:")
                                                                outputV1.result()

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputV1.balance < output5.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                            break
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputV1.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputV1.id:
                                                    break

                                        elif cardName != outputV1.name:
                                            print(
                                                "The name you input was not found")
                                            print(
                                                "Please enter a valid name again to avoid receiving error.")

                                        if cardName == outputV1.name:
                                            break
                                        elif cardName == outputV0.name:
                                            break

                                elif ba.lower() == outputM0.type.lower():

                                    while True:
                                        cardName = str(
                                            input("Enter your name: "))

                                        if cardName == outputM0.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputM0.id:
                                                    outputM0.result()
                                                    print(
                                                        "You have a balance of: ", outputM0.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output5.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputM0.balance > output5.productPrice:

                                                                print("Balance:", outputM0.balance, "-", "Product price:",
                                                                      output5.productPrice, " =", (outputM0.balance - output5.productPrice))

                                                                print(
                                                                    "Your total balance now is:")
                                                                outputM0.result()

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputM0.balance < output5.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputM0.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputM0.id:
                                                    break

                                        elif cardName == outputM1.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputM1.id:
                                                    outputM1.result()
                                                    print(
                                                        "You have a balance of: ", outputM1.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output5.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputM1.balance > output5.productPrice:

                                                                print("Balance:", outputM1.balance, "-", "Product price:",
                                                                      output5.productPrice, " =", (outputM1.balance - output5.productPrice))

                                                                print(
                                                                    "Your total balance now is:")
                                                                outputM1.result()

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputM1.balance < output5.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputM1.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputM1.id:
                                                    break

                                        elif cardName != outputM1.name:
                                            print(
                                                "The name you input was not found")
                                            print(
                                                "Please enter a valid name again to avoid receiving error.")
                                        else:
                                            print("Invalid input!!!")

                                        if cardName == outputM0.name:
                                            break
                                        elif cardName == outputM1.name:
                                            break

                                else:
                                    print("Invalid input 101!!!")
                                    print(
                                        "Please enter a valid card type to avoid receiving error.")

                                if ba.lower() == outputV0.type.lower():
                                    break
                                elif ba.lower() == outputM0.type.lower():
                                    break

                        elif decision.lower() == "No".lower():
                            print("Okay")
                            print(
                                "Comeback if you already decide to buy this item sir!")
                            break
                        else:
                            print("Invalid input 404!!!")
                            print(
                                "Please enter a valid answer to avoid receiving error.")

                        if decision.lower() == "Yes".lower():
                            break
                        elif decision.lower() == "No".lower():
                            break

                elif select.lower() == "Redmajic".lower():
                    output6.result()

                    print("Do you want to buy this sir?")

                    while True:
                        decision = str(input("").lower())

                        if decision.lower() == "Yes".lower():
                            print("Please enter your bank account")
                            print("We support Visa and MasterCard")
                            print(
                                "Please enter the following type of card you wanted to use :)")

                            while True:
                                ba = str(input("").lower())

                                if ba.lower() == outputV0.type.lower():

                                    while True:
                                        cardName = str(
                                            input("Enter your name: "))

                                        if cardName == outputV0.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputV0.id:
                                                    outputV0.result()
                                                    print(
                                                        "You have a balance of: ", outputV0.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output6.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputV0.balance > output6.productPrice:

                                                                print("Balance:", outputV0.balance, "-", "Product price:",
                                                                      output6.productPrice, " =", (outputV0.balance - output6.productPrice))

                                                                print(
                                                                    "Your total balance now is:")
                                                                outputV0.balance

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputV0.balance < output6.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                            break
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputV0.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputV0.id:
                                                    break

                                        elif cardName == outputV1.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputV1.id:
                                                    outputV1.result()
                                                    print(
                                                        "You have a balance of: ", outputV1.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output6.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputV1.balance > output6.productPrice:

                                                                print("Balance:", outputV1.balance, "-", "Product price:",
                                                                      output6.productPrice, " =", (outputV1.balance - output6.productPrice))

                                                                print(
                                                                    "Your total balance now is:")
                                                                outputV1.result()

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputV1.balance < output6.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                            break
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputV1.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputV1.id:
                                                    break

                                        elif cardName != outputV1.name:
                                            print(
                                                "The name you input was not found")
                                            print(
                                                "Please enter a valid name again to avoid receiving error.")

                                        if cardName == outputV1.name:
                                            break
                                        elif cardName == outputV0.name:
                                            break

                                elif ba.lower() == outputM0.type.lower():

                                    while True:
                                        cardName = str(
                                            input("Enter your name: "))

                                        if cardName == outputM0.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputM0.id:
                                                    outputM0.result()
                                                    print(
                                                        "You have a balance of: ", outputM0.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output6.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputM0.balance > output6.productPrice:

                                                                print("Balance:", outputM0.balance, "-", "Product price:",
                                                                      output6.productPrice, " =", (outputM0.balance - output6.productPrice))

                                                                print(
                                                                    "Your total balance now is:")
                                                                outputM0.result()

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputM0.balance < output6.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputM0.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputM0.id:
                                                    break

                                        elif cardName == outputM1.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputM1.id:
                                                    outputM1.result()
                                                    print(
                                                        "You have a balance of: ", outputM1.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output6.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputM1.balance > output6.productPrice:

                                                                print("Balance:", outputM1.balance, "-", "Product price:",
                                                                      output6.productPrice, " =", (outputM1.balance - output6.productPrice))

                                                                print(
                                                                    "Your total balance now is:")
                                                                outputM1.result()

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputM1.balance < output3.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputM1.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputM1.id:
                                                    break

                                        elif cardName != outputM1.name:
                                            print(
                                                "The name you input was not found")
                                            print(
                                                "Please enter a valid name again to avoid receiving error.")

                                        else:
                                            print("Invalid input!!!")

                                        if cardName == outputM1.name:
                                            break
                                        elif cardName == outputM0.name:
                                            break
                                else:
                                    print("Invalid input 101!!!")
                                    print(
                                        "Please enter a valid card type to avoid receiving error.")

                                if ba.lower() == outputV0.type.lower():
                                    break
                                elif ba.lower() == outputM0.type.lower():
                                    break

                        elif decision.lower() == "No".lower():
                            print("Okay")
                            print(
                                "Comeback if you already decide to buy this item sir!")
                            break
                        else:
                            print("Invalid input 404!!!")
                            print(
                                "Please enter a valid answer to avoid receiving error.")

                        if decision.lower() == "Yes".lower():
                            break
                        elif decision.lower() == "No".lower():
                            break

                elif select.lower() == "ROG".lower():
                    output7.result()

                    print("Do you want to buy this sir?")

                    while True:
                        decision = str(input("").lower())

                        if decision.lower() == "Yes".lower():
                            print("Please enter your bank account")
                            print("We support Visa and MasterCard")
                            print(
                                "Please enter the following type of card you wanted to use :)")

                            while True:
                                ba = str(input("").lower())

                                if ba.lower() == outputV0.type.lower():

                                    while True:
                                        cardName = str(
                                            input("Enter your name: "))

                                        if cardName == outputV0.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputV0.id:
                                                    outputV0.result()
                                                    print(
                                                        "You have a balance of: ", outputV0.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output7.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputV0.balance > output7.productPrice:

                                                                print("Balance:", outputV0.balance, "-", "Product price:",
                                                                      output7.productPrice, " =", (outputV0.balance - output7.productPrice))

                                                                print(
                                                                    "Your total balance now is:")
                                                                outputV0.balance

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputV0.balance < output7.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                            break
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputV0.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputV0.id:
                                                    break

                                        elif cardName == outputV1.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputV1.id:
                                                    outputV1.result()
                                                    print(
                                                        "You have a balance of: ", outputV1.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output7.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputV1.balance > output7.productPrice:

                                                                print("Balance:", outputV1.balance, "-", "Product price:",
                                                                      output7.productPrice, " =", (outputV1.balance - output7.productPrice))

                                                                print(
                                                                    "Your total balance now is:")
                                                                outputV1.result()

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputV1.balance < output7.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                            break
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputV1.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputV1.id:
                                                    break

                                        elif cardName != outputV1.name:
                                            print(
                                                "The name you input was not found")
                                            print(
                                                "Please enter a valid name again to avoid receiving error.")

                                        if cardName == outputV0.name:
                                            break
                                        elif cardName == outputV1.name:
                                            break

                                elif ba.lower() == outputM0.type.lower():

                                    while True:
                                        cardName = str(
                                            input("Enter your name: "))

                                        if cardName == outputM0.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputM0.id:
                                                    outputM0.result()
                                                    print(
                                                        "You have a balance of: ", outputM0.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output7.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputM0.balance > output7.productPrice:

                                                                print("Balance:", outputM0.balance, "-", "Product price:",
                                                                      output7.productPrice, " =", (outputM0.balance - output7.productPrice))

                                                                print(
                                                                    "Your total balance now is:")
                                                                outputM0.result()

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputM0.balance < output7.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputM0.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputM0.id:
                                                    break

                                        elif cardName == outputM1.name:

                                            while True:
                                                cardID = int(
                                                    input("Enter your Bank ID: "))

                                                if cardID == outputM1.id:
                                                    outputM1.result()
                                                    print(
                                                        "You have a balance of: ", outputM1.balance)

                                                    print(
                                                        "Do you want to pay this item?")
                                                    print(output7.productName)

                                                    while True:
                                                        decide = str(
                                                            input("Enter here: ").lower())

                                                        if decide.lower() == "Yes".lower():

                                                            if outputM1.balance > output7.productPrice:

                                                                print("Balance:", outputM1.balance, "-", "Product price:",
                                                                      output7.productPrice, " =", (outputM1.balance - output7.productPrice))

                                                                print(
                                                                    "Your total balance now is:")
                                                                outputM1.result()

                                                                print(
                                                                    "Thank you for buying our product :D")
                                                                print(
                                                                    "Come back again!")
                                                                break

                                                            elif outputM1.balance < output7.productPrice:
                                                                print("Oh!")
                                                                print(
                                                                    "You don't have enough money to buy this product :(")
                                                                print(
                                                                    "Sorry, but we cannot proceed this transaction")
                                                                print(
                                                                    "Please comeback if you have enough money to buy this item.")
                                                                print(
                                                                    "Have a nice day!")
                                                                break

                                                            else:
                                                                print(
                                                                    "System Error!!!")

                                                        elif decide.lower() == "No".lower():
                                                            print(
                                                                "Okay, thank you for trying to explore our product :)")
                                                            print(
                                                                "Have a nice day!")
                                                        else:
                                                            print(
                                                                "Invalid input!!!")

                                                        if decide.lower() == "Yes".lower():
                                                            break
                                                        elif decide.lower() == "No".lower():
                                                            break

                                                elif cardID != outputM1.id:
                                                    print("Wrong ID input!!!")

                                                elif cardID == str():
                                                    print("Invalid input!!!")
                                                    print(
                                                        "Please enter numerics only to avoid errors.")

                                                if cardID == outputM1.id:
                                                    break

                                        elif cardName != outputM1.name:
                                            print(
                                                "The name you input was not found")
                                            print(
                                                "Please enter a valid name again to avoid receiving error.")

                                        else:
                                            print("Invalid input!!!")

                                        if cardName == outputM0.name:
                                            break
                                        elif cardName == outputM1.name:
                                            break

                                else:
                                    print("Invalid input 101!!!")
                                    print(
                                        "Please enter a valid card type to avoid receiving error.")

                                if ba.lower() == outputV0.type.lower():
                                    break
                                elif ba.lower() == outputM0.type.lower():
                                    break

                        elif decision.lower() == "No".lower():
                            print("Okay")
                            print(
                                "Comeback if you already decide to buy this item sir!")
                            break
                        else:
                            print("Invalid input 404!!!")
                            print(
                                "Please enter a valid answer to avoid receiving error.")

                        if decision.lower() == "Yes".lower():
                            break
                        elif decision.lower() == "No".lower():
                            break
                else:
                    print("Invalid input 101!!!")
                    print("Please enter a valid phone to avoid receiving error.")

                if select.lower() == "Asus".lower():
                    break
                elif select.lower() == "Redmajic".lower():
                    break
                elif select.lower() == "ROG".lower():
                    break

        else:
            print("Invalid input 204!!!")
            print("Please enter a valid Brand type to avoid receiving error.")

        if user.lower() == "Smart Phone".lower():
            break
        elif user.lower() == "PC".lower():
            break

    break
