import pandas as pd
from sklearn import linear_model
df = pd.read_csv("house_with_missing_bedroom.csv")

df['Bedroom'] = df['Bedroom'].fillna(df['Bedroom'].mean())
print(df)

model = linear_model.LinearRegression()

model.fit(df[['Bedroom','Area','Age']],df['Price'])

prediction = model.predict([[3,2300,19]])

print(prediction)

df2 = pd.read_csv("sample.csv")