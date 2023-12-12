#1. A company is testing two different advertising strategies (A and B) to see which one 
#leads to higher click-through rates on their website. The click-through rates for 20 randomly 
#selected days under each strategy are given below. 
#Use the Mann-Whitney U test to determine if there is a significant difference in click-through 
#rates between the two strategies.
import numpy as np
from scipy.stats import bartlett
from scipy.stats import ttest_ind
from scipy.stats import mannwhitneyu
import pandas as pd 

s1 = np.array([1.2, 1.5, 1.8, 1.3, 1.6, 1.4, 1.7, 1.9, 1.2, 1.5, 1.8, 1.3, 1.6, 1.4, 1.7, 1.9, 1.2, 1.5, 1.8, 1.3])
s2 = np.array([1.1, 1.4, 1.7, 1.2, 1.5, 1.3, 1.6, 1.8, 1.1, 1.4, 1.7, 1.2, 1.5, 1.3, 1.6, 1.8, 1.1, 1.4, 1.7, 1.2])

result = mannwhitneyu(s1,s2)
print("p-value",result[1])

if result[1] < 0.05:
    print("We reject null hypothesis")
    print("There is significant differencec in two strategy")
else:
    print("We fail to reject null hypothesis")
    print("Variances may be same")    
    
#A study is conducted to comapre the commute times (in minutes)
#of two different routes(Route X and Route Y )to a Workplace. 
#The commute times for 15 randomly selected individuals for each 
#are provided below. use the mann-whitney U test to determine if 
#there is significant difference in commute times between the two routes

s1 = np.array([22, 25, 30, 28, 24, 27, 26, 23, 29, 31, 28, 25, 30, 27, 24])
s2 = np.array([35, 40, 38, 42, 37, 36, 39, 41, 38, 43, 40, 37, 42, 39, 36])

result = mannwhitneyu(s1,s2)
print("p-value",result[1])

if result[1] < 0.05:
    print("we reject null hypothesis")
    print("there is significant difference in two strategy")
else:
    print("we fail to reject null hypothesis")
    print("Variances may be same")
