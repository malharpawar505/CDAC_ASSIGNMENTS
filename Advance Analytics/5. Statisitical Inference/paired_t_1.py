import pandas as pd 
from scipy.stats import ttest_rel

anorexia = pd.read_csv("anorexia.csv")

FT = anorexia[anorexia['Treat']=='FT']

result = ttest_rel(FT['Prewt'], FT['Postwt'],
                   alternative="less")
print("P-Value =", result[1])

if result[1] < 0.05:
    print("We reject null hypothesis")
    print("The treatment FT may be effective")
else:
    print("We fail to reject null hypothesis")
    print("The treatment FT may not be effective")
    
# OR
result = ttest_rel(FT['Postwt'], FT['Prewt'],
                   alternative="greater")
print("P-Value =", result[1])

if result[1] < 0.05:
    print("We reject null hypothesis")
    print("The treatment FT may be effective")
else:
    print("We fail to reject null hypothesis")
    print("The treatment FT may not be effective")
    
######### CBT
CBT = anorexia[anorexia['Treat']=='CBT']

result = ttest_rel(CBT['Prewt'], CBT['Postwt'],
                   alternative="less")
print("P-Value =", result[1])

if result[1] < 0.05:
    print("We reject null hypothesis at 5% l.o.s")
    print("The treatment CBT may be effective")
else:
    print("We fail to reject null hypothesis at 5% l.o.s")
    print("The treatment CBT may not be effective")
    
    
######### Cont 
Cont = anorexia[anorexia['Treat']=='Cont']

result = ttest_rel(Cont['Prewt'], Cont['Postwt'],
                   alternative="less")
print("P-Value =", result[1])

if result[1] < 0.05:
    print("We reject null hypothesis at 5% l.o.s")
    print("The treatment Cont may be effective")
else:
    print("We fail to reject null hypothesis at 5% l.o.s")
    print("The treatment Cont may not be effective")
    
 
########## Breathing capacity
rheum = pd.read_csv("Rheumatic.csv")

result = ttest_rel(rheum['Before'], rheum['After'],
                   alternative="less")
print("P-Value =", result[1])

if result[1] < 0.05:
    print("We reject null hypothesis at 5% l.o.s")
    print("The treatment may be effective")
else:
    print("We fail to reject null hypothesis at 5% l.o.s")
    print("The treatment may not be effective")
    
#### Ohio

ohio = pd.read_csv("Ohio Education Performance.csv")

## Writing and reading
result = ttest_rel(ohio['Writing'], ohio['Reading'])
print("P-Value =", result[1])

if result[1] < 0.05:
    print("We reject null hypothesis at 5% l.o.s")
    print("There may be difference between writing and reading scores")
else:
    print("We fail to reject null hypothesis at 5% l.o.s")
    print("There may not be difference between writing and reading scores")

## Maths and Science
result = ttest_rel(ohio['Math'], ohio['Science'])
print("P-Value =", result[1])

if result[1] < 0.05:
    print("We reject null hypothesis at 5% l.o.s")
    print("There may be difference between Maths and Science scores")
else:
    print("We fail to reject null hypothesis at 5% l.o.s")
    print("There may not be difference between Maths and Science scores")


