import pandas as pd

data = {
    'Name': ['Fahim', 'Rabby', 'Jannat', 'Jahid', 'Mim'],
    'Age': [25, 30, 22, 24, 18],
    'City': ['Mirpur', 'Uttara', 'Dhanmondi', 'Savar', 'Dhamrai'],
    'CGPA': [2.5, 3.0, 2.2, 3.5, 3.8]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

print("Simple DataFrame")
print(df)

print("Display Columns")
name = df[["Name", "City"]]
print(name)