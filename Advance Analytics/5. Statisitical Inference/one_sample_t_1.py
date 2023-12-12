import pandas as pd 
import numpy as np 
from scipy.stats import t 
from scipy.stats import ttest_1samp

pg = pd.read_csv("PlantGrowth.csv")

s = pg['weight'].std()
xbar = pg['weight'].mean()
n = len(pg['weight'])
mu0 = 6

tstat = (xbar - mu0)/(s/np.sqrt(n))

print(t.cdf(tstat, 29))
print(t.sf(-tstat, 29))

p_val = t.cdf(tstat, 29)+t.sf(-tstat, 29)
print("P-Value =", p_val)

####################################################

######### 2 tailed #######################
result = ttest_1samp(pg['weight'], popmean=6)
print("Test stat =", result[0])
print("P-value =", result[1])

if result[1] < 0.05:
    print("We reject H0 at 5% l.o.s")
    print("Conclusion: The mean weight may not be 6")
else:
    print("We do not reject H0 at 5% l.o.s")
    print("Conclusion: The mean weight may be 6")

######## Lower tailed ###########

result = ttest_1samp(pg['weight'], popmean=6,
                     alternative="less")
print("Test stat =", result[0])
print("P-value =", result[1])

if result[1] < 0.05:
    print("We reject H0 at 5% l.o.s")
    print("Conclusion: The mean weight may be less than 6")
else:
    print("We do not reject H0 at 5% l.o.s")
    print("Conclusion: The mean weight may be greater than or equal to 6")
    
    
######## Problem 1

co2 = pd.read_csv("CO2.csv")

result = ttest_1samp(co2['uptake'], popmean=30,
                     alternative="less")
print("Test stat =", result[0])
print("P-value =", result[1])

if result[1] < 0.05:
    print("We reject H0 at 5% l.o.s")
    print("Conclusion: The mean uptake may be less than 30")
else:
    print("We do not reject H0 at 5% l.o.s")
    print("Conclusion: The mean uptake may be greater than or equal to 30")
   