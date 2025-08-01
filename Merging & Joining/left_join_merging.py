import pandas as pd

customer = {
    'CustomerID': [1, 2, 3, 4],
    'Name': ['Fahim', 'Rabby', 'Jahid', 'Mim']
}

order = {
    'CustomerID': [1, 2, 4, 5],
    'OrderAmount': [250, 500, 460, 320]
}

# Convert this dictionaries to DataFrames
df_customer = pd.DataFrame(customer)
df_order = pd.DataFrame(order)

df_merged = pd.merge(df_customer, df_order, on="CustomerID", how="left")
print("Left Join-")
print(df_merged)
