import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
# file_path = "ecommerce_sales.csv"

# df = pd.read_csv(file_path)
# print("✅ Phase 1 Complete: Data loaded successfully.")
# print("-"*40)

# print("Initial data info")
# print(df.head())

# print("Data types")
# print(df.dtypes)

# # Corrected line: Use 'Date' column and specify the format for robustness
# df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d', errors='coerce')
# print("✅ 'Date' column successfully converted to Datetime format.")

# # df['OrderId'] = pd.to_numeric(df['OrderId'])
# df['Quantity'] = pd.to_numeric(df['Quantity'])

# df.dropna(subset=['Date'],inplace=True)
# print(df.head())


# Category_sales = df.groupby('Category')['Total'].sum().reset_index()

# Category_sales = Category_sales.sort_values(by='Total',ascending=False)

# plt.figure(figsize=(10, 6))
# plt.bar(Category_sales['Category'], # X-axis: Categorical labels
#         Category_sales['Total'],    # Y-axis: Total sales value
#         color=['#4c72b0', '#c44e52', '#55a868', '#8172b2', '#ccb974']) # Custom colors

# # Using Labels and Title
# plt.title('Total Sales by Product Category', fontsize=16)
# plt.xlabel('Product Category', fontsize=12)
# plt.ylabel('Total Sales ($)', fontsize=12)

# # Rotate X-axis labels for better readability
# plt.xticks(rotation=45, ha='right') 
# plt.tight_layout()

# print("✅ Bar Chart Visualization Created for Category Sales.")

# # Display the plot
# plt.show()

x1 = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y1 = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope,intercept,r,p,a = stats.linregress(x1,y1)

def myfunc(x1):
        return slope * x1 + intercept

model = list(map(myfunc,x1))

plt.scatter(x1,y1)
plt.plot(x1,model)
plt.show()


# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]


# model1 = np.poly1d(np.polyfit(x,y,4))
# print(model1(40))
# line1 = np.linspace(1,22,100)
# plt.scatter(x,y)
# plt.plot(line1,model1(line1))
# plt.show()

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

model2 = np.poly1d(np.polyfit(x,y,3))
line2 = np.linspace(1,22,100)
plt.scatter(x,y)
plt.plot(line2,model2(line2))
plt.show()

