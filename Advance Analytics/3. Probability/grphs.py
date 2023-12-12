import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
os.chdir("C:/Training/Academy/Statistics (Python)/Datasets")

iris=pd.read_csv("iris.csv")

cars2018 = pd.read_csv("cars2018.csv")

sns.scatterplot(data=cars2018, x='Displacement',
                y='MPG', hue='Transmission')
plt.show()


g = sns.FacetGrid(cars2018, col="Transmission")
g.map(plt.scatter, "Displacement",  'MPG')
plt.show()


g = sns.FacetGrid(cars2018, row="Transmission")
g.map(plt.scatter, "Displacement",  'MPG')
plt.show()


g = sns.FacetGrid(cars2018, row="Transmission")
g.map(plt.hist, "Displacement")
plt.show()

