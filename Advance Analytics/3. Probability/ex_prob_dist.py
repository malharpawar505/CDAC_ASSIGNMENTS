from scipy.stats import binom , poisson
from scipy.stats import norm
import numpy as np 

print(binom.pmf(4, 150, 0.02))

print(poisson.pmf(4,3))


print(poisson.sf(14, 20))

print(poisson.pmf(0, 0.8))

print(poisson.pmf(25, 20))

print(poisson.sf(0, 3))

print(np.sum(poisson.pmf(np.arange(2,5), 3)))
#OR
print(poisson.cdf(4,3) - poisson.cdf(1,3))

print(poisson.pmf(1, 3))

print((65-50)/10)

print(norm.cdf(82,70,8 ))

print(norm.ppf(0.25, 60, 12))

print(norm.cdf(21,20,2) - norm.cdf(19,20,2))
