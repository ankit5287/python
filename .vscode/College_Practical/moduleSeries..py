import pandas as pd
data = pd.Series([1,3,5,7,9,11])
print(data)

list_data = data.tolist()
print(list_data)
print(type(list_data))