import random as rd
import matplotlib.pyplot as plt
import numpy as np

modulus = 2**32
def rng(seed):
    a = 1664525
    b = 1013904223  
    nextSeed =( (a*seed)+b ) % modulus
    return nextSeed / modulus

seed = 33 
n = 100000
nums = [];
for _ in range(n):
    nums.append(rng(seed))
    seed = rng(seed) * modulus

nums_sorted = np.sort(nums)
cdf = np.arange(1, len(nums_sorted)+1) / len(nums_sorted)

nums_inbuilt = [];
for _ in range(n):
    nums_inbuilt.append(rd.random() )

nums_inbuilt_sorted = np.sort(nums)
cdf_inbuilt = np.arange(1, len(nums_inbuilt_sorted)+1) / len(nums_inbuilt_sorted)

plt.subplot(1, 2, 1)
plt.plot(nums_sorted, cdf, color = 'g')
plt.title('CDF for question 1')
plt.xlabel('Data Value')
plt.ylabel('Cumulative Probability')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(nums_inbuilt_sorted, cdf_inbuilt, color='b') 
plt.title('Theoretical CDF using inbuit function')
plt.xlabel('Data Value')
plt.ylabel('Cumulative Probability')
plt.grid(True)

plt.show()
