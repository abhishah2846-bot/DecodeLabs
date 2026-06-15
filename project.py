import pandas as pd

df = pd.read_excel("data.xlsx")
print(df.isnull().sum())
#this is for finding the null values in the data set

df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

print(df.duplicated().sum())
#this is for finding the duplicate values in the data set
df = df.drop_duplicates()

df['Date'] = pd.to_datetime(df['Date'])
#this is for converting the date column to datetime format

df['Quantity'] = pd.to_numeric(df['Quantity'])
df['UnitPrice'] = pd.to_numeric(df['UnitPrice'])
df['ItemsInCart'] = pd.to_numeric(df['ItemsInCart'])
df['TotalPrice'] = pd.to_numeric(df['TotalPrice'])


df['Product'] = df['Product'].str.strip()
df['PaymentMethod'] = df['PaymentMethod'].str.strip()
df['OrderStatus'] = df['OrderStatus'].str.strip()
#this is for removing the leading and trailing spaces from the string columns

df['Product'] = df['Product'].str.strip()
df['PaymentMethod'] = df['PaymentMethod'].str.strip()
df['OrderStatus'] = df['OrderStatus'].str.strip()

df.to_excel("Cleaned_Dataset.xlsx", index=False)