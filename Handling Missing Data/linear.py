import pandas as pd

data = {
    'Name': ['Fahim', 'Shuvo', 'Jannat', 'Jahid', 'Mim', 'Masum', 'Mou'],
    'Age': [10, None, 20, None, 30, None, 40]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

print("Before interpolation")
print(df)

df["Age"] = df["Age"].interpolate(method="linear")
print("After interpolation")
print(df)