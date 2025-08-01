import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Jahid', 'Mim'],
    'Age': [25, 30, 22, 24, 18],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Savar', 'Dhaka'],
    'CGPA': [2.5, 3.0, 2.2, 3.5, 3.8]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

print("Sample DataFrame")
print(df)

print("Descriptive Statistics")
print(df.describe())