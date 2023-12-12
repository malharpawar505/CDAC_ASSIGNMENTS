import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
os.chdir("C:/Training/Academy/Statistics (Python)/Datasets")

cars2018 = pd.read_csv("cars2018.csv")

print(cars2018['Gears'].unique())
print(cars2018['Gears'].value_counts())

print(cars2018['Gears'].value_counts(normalize=True))
print(cars2018['Gears'].value_counts(normalize=True)*100)

cnt_df = cars2018['Gears'].value_counts(normalize=True).reset_index()

ex_v = np.sum(cnt_df['Gears']*cnt_df['proportion'])
print("E(X) =", ex_v)
print(cars2018['Gears'].mean())

#####################################################
x = np.arange(0,5 )
p = np.array([0.1, 0.2, 0.3, 0.3, 0.1])

ex_v = np.dot(x,p)
vx = np.dot(x**2, p) - (ex_v**2)
print("E(X) =", ex_v)
print("V(X) =", vx)

############ Joint ################

cars2018['Intake Valves Per Cyl'].value_counts()
cars2018['Gears'].value_counts()

## Cross Tabulation
pd.crosstab(index=cars2018['Gears'], 
            columns=cars2018['Intake Valves Per Cyl'],
            margins=True)
### Joint Prob
pd.crosstab(index=cars2018['Gears'], 
            columns=cars2018['Intake Valves Per Cyl'],
            margins=True, normalize=True)

### Conditional Prob by Columns
pd.crosstab(index=cars2018['Gears'], 
            columns=cars2018['Intake Valves Per Cyl'],
            margins=True, normalize='columns')

### Conditional Prob by Rows
pd.crosstab(index=cars2018['Gears'], 
            columns=cars2018['Intake Valves Per Cyl'],
            margins=True, normalize='index')

## Cross Tabulation
pd.crosstab(index=cars2018['Transmission'], 
            columns=cars2018['Aspiration'],
            margins=True)
### Joint Prob
pd.crosstab(index=cars2018['Transmission'], 
            columns=cars2018['Aspiration'],
            margins=True, normalize=True)

###########  Survey.csv ################
survey = pd.read_csv("survey.csv")

### Joint Prob
pd.crosstab(index=survey['Exer'], 
            columns=survey['Smoke'],
            margins=True, normalize=True)

pd.crosstab(index=survey['Exer'], 
            columns=survey['Smoke'],
            margins=True, normalize='columns')


############ Num 1 ##############################
p = np.array([[0.040379,0.115286,0.115051,0.0989],
              [0.053722,0.115051,0.088249,0.028675],
              [0.046231,0.0989,0.096091,0.103464]])

prob = pd.DataFrame(p, 
                    columns=['100kg','200kg','300kg','500kg'],
                    index = ['100kg','300kg','500kg'])
print("Marginal for Demand:", prob.sum())
print("Marginal for Supply:", prob.sum(axis=1))

print("Conditional for Supp=300kg:")
print(prob.loc['300kg']/np.sum(prob.loc['300kg']))

print("Conditional for Dem=300kg:")
print(prob['300kg']/np.sum(prob['300kg']))














