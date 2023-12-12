import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
os.chdir("C:/Training/Academy/Statistics (Python)/Datasets")

iris=pd.read_csv("iris.csv")

sns.boxplot(data=iris, y='Sepal.Width')
plt.show()

q3 = iris['Sepal.Width'].quantile(0.75)
q1 = iris['Sepal.Width'].quantile(0.25)
iqr = q3 - q1

upper = iris[iris['Sepal.Width']>q3 + 1.5*iqr]
lower = iris[iris['Sepal.Width']<q1 - 1.5*iqr]
print("Upper Outliers:\n", upper['Sepal.Width'].values)
print("Lower Outliers:\n", lower['Sepal.Width'].values)


sns.boxplot(data=iris, y='Sepal.Length')
plt.show()

col_name = 'Sepal.Length'
q3 = iris[col_name].quantile(0.75)
q1 = iris[col_name].quantile(0.25)
iqr = q3 - q1

upper = iris[iris[col_name]>q3 + 1.5*iqr]
lower = iris[iris[col_name]<q1 - 1.5*iqr]
print("Upper Outliers:\n", upper[col_name].values)
print("Lower Outliers:\n", lower[col_name].values)

def find_outliers(df,col_name):
    q3 = df[col_name].quantile(0.75)
    q1 = df[col_name].quantile(0.25)
    iqr = q3 - q1

    upper = df[df[col_name]>q3 + 1.5*iqr]
    lower = df[df[col_name]<q1 - 1.5*iqr]
    print("Upper Outliers:\n", upper[col_name].values)
    print("Lower Outliers:\n", lower[col_name].values)

find_outliers(iris,'Sepal.Width')

air = pd.read_csv("Airquality.csv")

sns.boxplot(data=air, y='Wind')
plt.show()

find_outliers(df=air, col_name='Wind')

#################################
cars2018 = pd.read_csv("cars2018.csv")

sns.boxplot(data=cars2018, y='MPG')
plt.show()

find_outliers(df=cars2018, col_name='MPG')

sns.boxplot(data=cars2018, y='MPG', x='Transmission')
plt.show()

ss = cars2018[cars2018['Transmission']=='Manual']
find_outliers(df=ss, col_name='MPG')

for col in cars2018['Transmission'].unique():
    ss = cars2018[cars2018['Transmission']==col]
    print("Transmission -", col)
    find_outliers(df=ss, col_name='MPG')




