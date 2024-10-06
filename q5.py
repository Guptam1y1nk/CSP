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
my_nums = [];
for _ in range(n):
    my_nums.append(rng(seed))
    seed = rng(seed) * modulus

nums = np.array(my_nums)

# Gaussian distribution
u1 = nums 
my_nums_2 = [];
for _ in range(n):
    my_nums_2.append(rng(seed))
    seed = rng(seed) * modulus

u2 = np.array(my_nums_2)

gaussian_RV = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)

# Lognormal Distribution
lognormal_RV = np.exp(gaussian_RV)

def plot_cdf(nums, ax, title):
    nums_sorted = np.sort(nums)
    cdf = np.arange(1, len(nums_sorted) + 1) / len(nums_sorted)
    ax.plot(nums_sorted, cdf, marker=".", linestyle="none")
    ax.set_title(title)
    ax.set_xlabel('Value')
    ax.set_ylabel('Cumulative Probability')
    ax.grid(True)

# Create subplots for the CDFs
fig, axes = plt.subplots(1,2, figsize=(18, 5))

# Plot each CDF
plot_cdf(gaussian_RV, axes[0], 'CDF of Gaussian Distribution')
plot_cdf(lognormal_RV, axes[1], 'CDF of Lognormal Distribution')

plt.tight_layout()
plt.show()
