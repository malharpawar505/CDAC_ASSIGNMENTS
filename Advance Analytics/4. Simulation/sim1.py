import numpy as np
import pandas as pd 

np.random.seed(67) # getting reproducible output
a = np.random.rand(100)
print(a)

trials = ["H" if i>0.5 else "T" for i in a]
print(np.unique(trials, return_counts=True))


np.random.seed(67) # getting reproducible output
a = np.random.rand(10000)
print(a)

x = [1,4,8]

sim=[]
for i in range(0,len(a)):
    if a[i] < 0.3:
        sim.append(1)
    elif a[i]>=0.3 and a[i]<0.8:
        sim.append(4)
    else:
        sim.append(8)
        
print(np.unique(sim, return_counts=True))
print(np.mean(sim))

######### in short ################
x = np.array([1,4,8])
probs = np.array([0.3,0.5,0.2])
cums = np.cumsum(probs)

rnd = np.random.rand(100)
# for finding any value
d = 0.6
finding = d > cums
i_finding = np.sum(finding)
x[i_finding]

# loop for finding
sim = []
for d in rnd:
    finding = d > cums   
    i_finding = np.sum(finding)
    sim.append(x[i_finding])

########### Sick Drivers ##############
x = np.arange(0,6)
probs = np.array([0.3,0.2,0.15,0.1,0.13,0.12])
cums = np.cumsum(probs)
np.random.seed(67) # getting reproducible output
rnd = np.random.rand(30)

sim = []
for d in rnd:
    finding = d > cums   
    i_finding = np.sum(finding)
    sim.append(x[i_finding])

print(np.unique(sim, return_counts=True))
print("E(X) =", np.dot(x,probs))
print("Mean of Sim =", np.mean(sim))

def simulate(x,probs,seed,nos):
    cums = np.cumsum(probs)
    np.random.seed(seed) # getting reproducible output
    rnd = np.random.rand(nos)

    sim = []
    for d in rnd:
        finding = d > cums   
        i_finding = np.sum(finding)
        sim.append(x[i_finding])
    return sim;

# simulate(x=x, probs=probs, seed=54, nos=100)


supply = np.arange(10,60,10 )
freq_supp = np.array([40,50,190,150,70])
prob_supp = freq_supp/np.sum(freq_supp)

sim_supp = simulate(x=supply, 
                    probs=prob_supp, seed=54, nos=30)

demand = np.arange(10,60,10 )
freq_dem= np.array([50,110,200,100,40])
prob_dem = freq_dem/np.sum(freq_dem)

sim_dem = simulate(x=demand, 
                    probs=prob_dem, seed=66, nos=30)


df_sim = pd.DataFrame({'Supp':sim_supp,
                       'Dem':sim_dem})
df_sim['sold'] = np.minimum(df_sim['Supp'], df_sim['Dem'])
df_sim['loss'] = df_sim['Supp'] - df_sim['sold']
df_sim['p/l'] = df_sim['sold']*10 - df_sim['loss']*8
print("Total P/L = ", df_sim['p/l'].sum())


####### Simulation of Binomial for Ins Agent ###
from scipy.stats import binom 

print(binom.stats(40,0.25))
sim_mon = binom.rvs(40,0.25,size=60, random_state=23)
print("Mean of Sim =", np.mean(sim_mon)) 

##### Simulation of Poisson for accidents ####
from scipy.stats import poisson 

print(poisson.rvs(12, size=10, random_state=23))
print(poisson.stats(12))
sim_mon = poisson.rvs(12, size=10, random_state=23)
print("Mean of Sim =", np.mean(sim_mon)) 




