import pandas as pd

data = {
    'Name': ['Fahim', 'Fardin', 'Jannat', 'Jahid', 'Mim'],
    'Age': [25, 24, 22, 24, 22],
    'City': ['Mirpur', 'Gulshan', 'Dhanmondi', 'Savar', 'Dhamrai'],
    'Salary': [25000, 38000, 22000, 35000, 28000]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

grouped = df.groupby("Age")["Salary"].sum()
print(grouped)
