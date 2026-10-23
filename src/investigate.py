import pandas as pd

df = pd.read_csv("../data/sales_january.csv")

#looking at the data
print(df.head)

print(df.shape)

print(df.columns)

print(df.dtypes)

print(df.info())

print (df.isnull().sum())

#checking the null row
print(df[df["customer_id"].isnull()])

print (df[df["product"].isnull()])

#check duplicate

print(df["transaction_id"].unique())
print(df[df.duplicated()])
print(df["transaction_id"].nunique())
print(
    df[df["transaction_id"].duplicated(
        keep = False)]
)




