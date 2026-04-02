import pandas as pd

data = {
    "Name": ["Jeffrey", "Veronica"],
    "Age": [20, 21],
    "Score": [90, 91]
}

result = pd.DataFrame(data)
print(result)

print(result.loc[1, "Score"])
print(result.loc[1, ["Score", "Age"]])
