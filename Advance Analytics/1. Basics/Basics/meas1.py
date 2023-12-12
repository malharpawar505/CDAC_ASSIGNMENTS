import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
os.chdir("C:/Training/Academy/Statistics (Python)/Datasets")

iris=pd.read_csv("iris.csv")

print(iris['Sepal.Length'].mean())
print(iris['Sepal.Length'].median())

print("1st Quartile =", iris['Sepal.Length'].quantile(0.25))
print("2nd Quartile =",iris['Sepal.Length'].quantile(0.5))
print("3rd Quartile =",iris['Sepal.Length'].quantile(0.75))

print("All Quartiles:\n",
      iris['Sepal.Length'].quantile([0.25, 0.5, 0.75]))

print("60th Percentile=",iris['Sepal.Length'].quantile(0.6))

plt.boxplot(iris['Sepal.Length'])
plt.title("Box Plot")
plt.show()


plt.boxplot(iris['Sepal.Width'])
plt.title("Box Plot")
plt.show()


plt.boxplot(iris['Petal.Length'])
plt.title("Box Plot")
plt.show()


plt.boxplot(iris['Petal.Width'])
plt.title("Box Plot")
plt.show()

### Using seaborn
sns.boxplot(data=iris, y='Sepal.Length')
plt.show()

print("All Quartiles:\n",
      iris.groupby('Species')['Sepal.Length'].quantile([0.25, 0.5, 0.75]))

sns.boxplot(data=iris, y='Sepal.Length',
            x='Species')
plt.show()

sns.boxplot(data=iris, y='Petal.Length',
            x='Species')
plt.show()

print("Population Variance:")
print(iris['Sepal.Length'].var(ddof=0))
# OR
print(sum((iris['Sepal.Length'] - iris['Sepal.Length'].mean())**2)/150)


print("Sample Variance:")
print(iris['Sepal.Length'].var())
# OR
print(sum((iris['Sepal.Length'] - iris['Sepal.Length'].mean())**2)/149)

print("Sample SD:")
print(iris['Sepal.Length'].std())

print(iris['Sepal.Length'].describe())

### Skewness
print(iris['Sepal.Length'].skew())

plt.hist(iris['Sepal.Length'], bins=7)
plt.title("Histogram")
plt.show()

print(iris['Petal.Length'].skew())

plt.hist(iris['Petal.Length'], bins=7)
plt.title("Histogram")
plt.show()

print(iris['Petal.Width'].skew())

plt.hist(iris['Petal.Width'], bins=7)
plt.title("Histogram")
plt.show()

print(iris['Sepal.Width'].skew())

plt.hist(iris['Sepal.Width'], bins=7)
plt.title("Histogram")
plt.show()

diams = pd.read_csv("diamonds.csv")

print(diams['price'].skew())

plt.hist(diams['price'], bins=7)
plt.title("Histogram")
plt.show()

### Kurtosis
print(diams['price'].kurtosis())
print(iris['Sepal.Length'].kurtosis())
