import pandas as pd

data = {
    'Name': ['Fahim', 'Fardin', 'Jannat', 'Jahid', 'Mim'],
    'Age': [25, 30, 22, 24, 18],
    'City': ['Mirpur', 'Gulshan', 'Dhanmondi', 'Savar', 'Dhamrai'],
    'CGPA': [2.5, 3.8, 2.2, 3.5, 2.8]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

df.sort_values(by=["Age","CGPA"], ascending=[True, False], inplace=True)
print(df)