import pandas as pd
import matplotlib.pyplot as plt
file_path = "ecommerce_sales.csv"

df = pd.read_csv(file_path)
print("✅ Phase 1 Complete: Data loaded successfully.")
print("-"*40)

print("Initial data info")
print(df.head())

print("Data types")
print(df.dtypes)

# Corrected line: Use 'Date' column and specify the format for robustness
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d', errors='coerce')
print("✅ 'Date' column successfully converted to Datetime format.")

# df['OrderId'] = pd.to_numeric(df['OrderId'])
df['Quantity'] = pd.to_numeric(df['Quantity'])

df.dropna(subset=['Date'],inplace=True)
print(df.head())


Category_sales = df.groupby('Category')['Total'].sum().reset_index()

Category_sales = Category_sales.sort_values(by='Total',ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(Category_sales['Category'], # X-axis: Categorical labels
        Category_sales['Total'],    # Y-axis: Total sales value
        color=['#4c72b0', '#c44e52', '#55a868', '#8172b2', '#ccb974']) # Custom colors

# Using Labels and Title
plt.title('Total Sales by Product Category', fontsize=16)
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)

# Rotate X-axis labels for better readability
plt.xticks(rotation=45, ha='right') 
plt.tight_layout()

print("✅ Bar Chart Visualization Created for Category Sales.")

# Display the plot
plt.show()