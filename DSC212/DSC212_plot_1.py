import numpy as np
import matplotlib.pyplot as plt
 

#For IID Random variables 

n_values = list(range(1, 1001))
sample_means = [np.random.normal(0, 1, n).mean() for n in n_values]

plt.figure(figsize=(10, 6))
plt.plot(n_values, sample_means, label='Sample Mean',color="magenta")
plt.xlabel('Sample Size (n)')
plt.ylabel('Sample Mean')
plt.title('Sample Mean vs Sample Size')
plt.legend()
plt.grid(True)
plt.show()

#For Cauchy

sample_means_ch = [np.random.standard_cauchy(n).mean() for n in n_values]

plt.figure(figsize=(10, 6), )
plt.plot(n_values, sample_means_ch, label='Sample Mean')
plt.xlabel('Sample Size (n)')
plt.ylabel('Sample Mean')
plt.title('Sample Mean vs Sample Size')
plt.legend()
plt.grid(True)
plt.show()