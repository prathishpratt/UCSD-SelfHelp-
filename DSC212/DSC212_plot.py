import numpy as np
import matplotlib.pyplot as plt
import math
import os
from scipy.stats import norm

sample_size = 100    
trails = 100 
a_values = [-2, -1, -0.5, -0.25, 0, 0.25, 0.5, 1, 2]

results = np.zeros((trails, len(a_values)))

#Population mean - 0.5 - see derivation in submission
popmean = 0.5

for i in range(trails):
    sample = np.random.rand(sample_size)
    sammean = np.mean(sample)
    samvar = np.var(sample)
    
    z = (sammean - popmean) / np.sqrt(samvar/sample_size)   # Get Z score
    
    for j, a in enumerate(a_values):
        if z<=a:
            results[i,j]=1
        else:
            results[i,j]=0
            
            
# Z-SCORE

column_sum = np.sum(results, axis=0)

# Calculate the CDF of N(0, 1)
x = np.linspace(-2, 2, 10000)
cdf_n = norm.cdf(x)

fig, (a, b) = plt.subplots(1, 2, figsize=(18,9))

# Plot the count against the values for a

a.plot(a_values, column_sum, linestyle = 'dashdot', label="Column Sums", color="magenta")
#a.set_facecolor('tab:blue')
a.patch.set_facecolor('black')
a.set_title("The number of times Zn ≤ a") 
a.set_xlabel ("a") 
a.set_ylabel("Count of Z-score <= a") 
a.grid()

# Plot the CDF of Standard Normal Distribution - N(0,1)
b.plot(x, cdf_n, label = 'N(0,1) CDF', linestyle = 'dashdot',color="cyan")
b.patch.set_facecolor('black')
b.set_title("Std Normal Distribution N(0, 1)")
b.set_xlabel ("a")
b.set_ylabel("Probability")
b.grid()