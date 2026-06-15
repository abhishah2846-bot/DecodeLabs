import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_excel("data.xlsx")


print(df.head())
print(df.info())
print(df.shape)

#Descriptive Statistics 
print("Mean values")
print(df[['Quantity','UnitPrice','TotalPrice']].mean())

print("Median values")
print(df[['Quantity','UnitPrice','TotalPrice']].median())

print("Mode values")
print(df[['Quantity','UnitPrice','TotalPrice']].mode())

print("Count Values")
print(df[['Quantity','UnitPrice','TotalPrice']].count())    

product_counts = df['Product'].value_counts()
print("\nProduct Counts:")
print(product_counts)

product_sales = df.groupby("Product")["TotalPrice"].sum() 
print("\nTotal Sales by Product:")
print(product_sales)

# outlier Detection
Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["TotalPrice"] < lower_limit) |
    (df["TotalPrice"] > upper_limit)
]

print("\nOUTLIERS FOUND:")
print(outliers)
print("\nNUMBER OF OUTLIERS:")
print(len(outliers))


#Visualization
#First Chart: Total Sales by Product
plt.figure(figsize=(8,5))
product_sales.plot(kind='bar')
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales (₹)") 
plt.show()

# Second Chart: Product Popularity
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

sns.countplot(
    data=df, 
    x='Product', 
    order=df['Product'].value_counts().index, 
    palette='viridis'                        
)

plt.title('Product Popularity (Total Orders by Category)', fontsize=16, fontweight='bold')
plt.xlabel('Product Name', fontsize=12)
plt.ylabel('Number of Orders', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Pie chart for Payment Method Preferences
plt.figure(figsize=(8, 6))
payment_counts = df['PaymentMethod'].value_counts()

plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', startangle=140, 
        colors=sns.color_palette('pastel'), wedgeprops={'edgecolor': 'white', 'linewidth': 2})


centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Payment Method Preferences', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()