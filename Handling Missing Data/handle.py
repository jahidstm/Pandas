import pandas as pd

data = {
    'Name': ['Fahim', None, 'Jannat', 'Jahid', 'Mim'],
    'Age': [25, None, 22, 24, 18],
    'City': ['Mirpur', None, 'Dhanmondi', 'Savar', 'Dhamrai'],
    'CGPA': [2.5, None, 2.2, 3.5, 3.8]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

print("Simple DataFrame")
print(df)

df.dropna(inplace=True)
print(df)