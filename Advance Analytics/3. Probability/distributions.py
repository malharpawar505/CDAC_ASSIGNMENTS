from scipy.stats import binom, poisson, norm
import numpy as np

## binom.pmf(0,40,0.25) + binom.pmf(1,40,0.25) +....

s = 0
for i in range(0, 11):
    s += binom.pmf(i,40,0.25)
    
print("CDF=",s)
# OR
print(np.sum(binom.pmf(np.arange(0, 11), 40, 0.25)))
# OR
print(binom.cdf(10,40,0.25))

print(binom.sf(19,40,0.25))

print(binom.stats(40,0.25))


#####################################

binom.pmf(5, 20, 0.15)

binom.sf(12, 20, 0.15)

binom.cdf(10, 20, 0.15)

###########################################
 
poisson.pmf(5, 12)

poisson.cdf(12,12)

poisson.sf(14, 12)

print(np.sum(poisson.pmf(np.arange(10,16), 12)))
#OR
print(poisson.cdf(15,12) - poisson.cdf(9,12))

##############
poisson.sf(5,4)

poisson.cdf(2,4)

#####################################

norm.cdf(58, 64, 4)

norm.sf(200, 180, 30)

##########
norm.sf(2000, 1678, 500)

norm.ppf(0.9, 1678, 500)











