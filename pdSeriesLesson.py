import pandas as pd

print("Welcome!")
print("These is a system that listed all individuals who has youngest age and oldest age.")
print("All individuals here displayed their ages from the lowest to highest accordingly")
print("And these people's are:")
print("Jeffrey")
print("Anna")
print("Inuzawa")
print("John")
print("Veronica")

age = pd.Series([20, 21, 22, 23, 24], index=["Jeffrey",
                "Anna", "Inuzawa", "John", "Veronica"])

print("The youngest one is: Jeffrey")
print(age.loc["Jeffrey"])

print("The oldest one is: ")
print(age.loc["Veronica"])

print("These section will display all the individuals age's (In alphabitcal order)")

sorted_by_names = age.sort_index()
print(sorted_by_names)
print("The youngest one is: Jeffrey")
print(sorted_by_names.loc["Jeffrey"])
print("The oldest one is: Veronica")
print(sorted_by_names.loc["Veronica"])

sorted_by_age = age.sort_values()
print("These section will display their names according to their age (from lowest to highest)")
print(sorted_by_age)
print("The youngest one is: Jeffrey")
print(sorted_by_age.loc["Jeffrey"])
print("The oldest one is: Veronica")
print(sorted_by_age.loc["Veronica"])
