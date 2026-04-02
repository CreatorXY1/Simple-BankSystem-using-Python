class Garage:

    def __init__(self, name, color, year):
        self.__name = name
        self.__color = color
        self.__year = year

    def listSC(self):
        print(self.__name, "has been added to the garage.")

    def listRC(self):
        print(self.__name, "has been added to the garage.")


class SportsCar():

    def __init__(self, name, color, year, topspeed):
        self.__name = name
        self.__color = color
        self.__year = year
        self.__topspeed = topspeed

    def result(self):
        print("Searching for cars with year 2025 and color Silver Gray...")
        if self.__color == "Silver Gray" and self.__year == 2025:
            print("The brand name of the car is", self.__name,
                  "and hold the title as a greatest car in the world since", self.__year)
            print("The top speed can it reach is:", self.__topspeed)
        else:
            print("No car found with color Blue")


class RegularCar():

    def __init__(self, name, color, year, topspeed):
        self.__name = name
        self.__color = color
        self.__year = year
        self.__topspeed = topspeed

    def result(self):
        print("Searching for cars with year 2018 and color Red...")
        if self.__color == "Red" and self.__year == 2018:
            print("The brand name of the car is", self.__name,
                  "with color", self.__color, "that released in", self.__year)
            print(self.__name, "has been removed from the garage.")
        else:
            print("No car found with year 2018 and color Red.")


car1 = Garage("Bugati", "Silver Gray", 2025)
car2 = Garage("Ducati", "Red", 2019)
car3 = SportsCar("Bugati", "Silver Gray", 2025, 733.92)
car4 = RegularCar("Ducati", "Red", 2019, 677.33)

car1.listSC()
car2.listRC()
car3.result()
car4.result()
