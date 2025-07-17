import pandas as pd

# Create a simple dataset using a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Show the DataFrame
print("Original DataFrame:")
print(df)

# Filter rows where Age is greater than 23
filtered_df = df[df['Age'] > 23]

print("\nFiltered DataFrame (Age > 23):")
print(filtered_df)
