import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)
print(df)

df.to_csv("output.csv", index=False)