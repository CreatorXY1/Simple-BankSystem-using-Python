# This is a sample Python code that demonstrates various programming concepts such as variables, conditionals, loops, functions, classes, inheritance, and encapsulation.

# This section demonstrates the use of if-else statements to evaluate a boolean variable.
aBoolean = False

if aBoolean:
    print("It is true!")
else:
    print("It is false!")

# -----------------------------------------------------

# This section demonstrates the use of for loops to iterate over a range of numbers
for i in range(5):
    print("Loop number:", i)

# -----------------------------------------------------

# This section demonstrates the use of while loops to execute a block of code as long as a condition is true.
count = 3

while count >= 1:
    print("Loading...")
    count = count - 1

for age in range(3):
    print(18 + age)


# -----------------------------------------------------

# This section demonstrates the use of functions to encapsulate reusable blocks of code.
def say_hello(greeting):
    print("Hello World!")
    print(greeting)


say_hello("Hello, Jeffrey!")


def greet_user(username):
    print("Hello, ", username)


greet_user("Jeffrey!")

# -----------------------------------------------------

# This section demonstrate the use of classes and objects to create reusable blueprints for creating objects with specific attributes and behaviors.


class Car0:

    def __init__(self, color, brand, year):
        self.color = color
        self.year = year
        self.brand = brand

    def result(self):
        print("The car is a", self.color, self.brand, "from", self.year)


c1 = Car0("Silver Gray", "Bugati", 2025)
c2 = Car0("Red", "Ducati", 2026)

c1.result()
c2.result()

# -----------------------------------------------------

# This section demonstrates the use of inheritance to create a new class that inherits attributes and behaviors from a parent class.


class Car1:

    def __init__(self, color, brand, year):
        self.color = color
        self.brand = brand
        self.year = year

    def carIntro(self):
        print("The brand of this car is", self.brand,
              "with lovely color which is", self.color)
        print('The car once called "The Great Golden Horse" is era since', self.year)


class SportsCarToday(Car1):

    def __init__(self, color, brand, year, top_speed):
        super().__init__(color, brand, year)
        self.ts = top_speed

    def scIntro(self):
        print("Introducing")
        print("The most fastest car in today")
        print("Brand:", self.brand, "\n", "Color:", self.color, "\n",
              "Year:", self.year, "\n", "Horse Power:", self.ts)
        print("Vs")


class SportsCarHistory(Car1):

    def __init__(self, color, brand, year, top_speed):
        super().__init__(color, brand, year)
        self.ts = top_speed

    def scIntro(self):
        print("The most fastest car in history")
        print("Brand:", self.brand, "\n", "Color:",
              self.color, "\n", "Year:", self.year, "\n", "Horse Power:", self.ts)


c1 = SportsCarToday("Silver Gray", "BUGATI", 2026, 198544)
c2 = SportsCarHistory("Golden Horse", "Lamborgini", 1990, 197800)
c3 = Car1("Golden Horse", "Lamborgini", 1990)

c3.carIntro()
c1.scIntro()
c2.scIntro()

# --------------------------------------------------------------------------------------

# This section demonstrates the use of polymorphism to allow objects of different classes to be treated as objects of a common superclass, while still maintaining their own unique behaviors.


class Car2:

    def drive(self):
        print("drives smoothly")


class SportsCar0(Car2):

    def drive(self):
        print("drives at lightning speed")


c1 = Car2()
c2 = SportsCar0()

c1.drive()
c2.drive()

# --------------------------------------------------------------------------------------

# This section demonstrates the use of encapsulation to restrict access to certain attributes and methods of a class, while still providing public methods to interact with those attributes.


class BankAccount:
    def balance(self, balance):
        self.__balance = balance

    def tax(self, tax):
        self.__balance -= tax

    def result(self):
        return self.__balance


account = BankAccount()

account.balance(500)
account.tax(300)

print("Your balance is:", account.result())
