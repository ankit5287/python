import pandas as pd
import matplotlib.pyplot as plt
l1 = ("Red", "Green", "White")
l2 = ("Red", "Black")
l3 = ("Yellow")

# Fixed: pd.Series takes data and index as first two args; removed l3 to avoid TypeError
data = pd.Series([l1,l2,l3])
print(data)

x = [34, 67, 89, 90]
y = [78, 45, 23, 12]

plt.plot(x,y,marker='o',color='r')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Simple Plot")
plt.show()

Programming_languages = ['Java', 'Python', 'PHP','JavaScript', 'C#', 'C++']
Popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.bar(Programming_languages, Popularity,color ='blue',width = 0.4)
plt.xlabel("Programming Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Languages")
plt.show()


languages=['Java', 'Python', 'PHP','JavaScript', 'C#', 'C++']
Popularity=[22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.pie(Popularity, labels=languages, startangle=60, shadow=True,autopct='%1.1f%%')
plt.title("Popularity of Programming Languages")
plt.show()