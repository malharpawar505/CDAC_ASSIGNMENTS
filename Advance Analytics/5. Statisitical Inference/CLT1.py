from scipy.stats import binom 
import numpy as np 
import matplotlib.pyplot as plt 

#### CLT #########
s_size = 500000

s_means = []
for i in range(0,100):
    sim = binom.rvs(40, 0.25, size=s_size)
    m_sim = np.mean(sim)
    s_means.append(m_sim)

plt.hist(s_means)
plt.title("Sample Size ="+ str(s_size))
plt.show()

