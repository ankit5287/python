import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
df = pd.read_csv("house_data.csv")

x = df[['Area_sqft']]
y = df['Price_Lakh']

model = linear_model.LinearRegression()
model.fit(x,y)
prediction = model.predict([[3000]])
print(prediction)

plt.scatter(x,y)
plt.show()