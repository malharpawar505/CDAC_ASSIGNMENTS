import pandas as pd 
from scipy.stats import ttest_1samp 

consum = pd.read_excel("Consumer Transportation Survey.xlsx",
                       skiprows=2)

col = consum['# of hours per week in vehicle']

result = ttest_1samp(col, popmean=8, alternative='less')
print("P-value =", result[1])

if result[1] < 0.05:
    print("We reject null hypothesis")
    print("Hours may be less than 8")
else:
    print("We fail to reject null hypothesis")
    print("Hours may be atleast 8")    
    
col = consum['Miles driven per week']
result = ttest_1samp(col, popmean=600)
print("P-value =", result[1])

if result[1] < 0.05:
    print("We reject null hypothesis")
    print("Miles driven per week may not be 600")
else:
    print("We fail to reject null hypothesis")
    print("Miles driven per week may be 600")    


suv = consum[consum['Vehicle Driven']=="SUV"]
col = suv['Age']

result = ttest_1samp(col, popmean=35, alternative='greater')
print("P-value =", result[1])

if result[1] < 0.05:
    print("We reject null hypothesis")
    print("Age of SUV drivers may be greater than 35")
else:
    print("We fail to reject null hypothesis")
    print("Age of SUV drivers may not be greater than 35")    





