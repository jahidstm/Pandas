import pandas as pd

reg1 = {
    'CustomerID': [1, 2, 3],
    'Name': ['Fahim', 'Rabby', 'Jahid']
}

reg2 = {
    'CustomerID': [4, 5, 6],
    'Name': ['Rakib', 'Abir', 'Arko']
}

# Convert this dictionaries to DataFrames
df_reg1 = pd.DataFrame(reg1)
df_reg2 = pd.DataFrame(reg2)

df_concat = pd.concat([df_reg1, df_reg2], axis=0, ignore_index=True)
print(df_concat)
