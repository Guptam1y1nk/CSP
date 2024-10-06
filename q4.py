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

# Exponential distribution
lambda_param = 1
exponential_RV = -lambda_param * np.log(1 - nums)

# Pareto distribution
alpha_param = 2  
x_m = 1          
pareto_RV = x_m * (1 - nums ) ** (-1 / alpha_param)

# Gaussian distribution
u1 = nums 
my_nums_2 = [];
for _ in range(n):
    my_nums_2.append(rng(seed))
    seed = rng(seed) * modulus

u2 = np.array(my_nums_2)

gaussian_RV = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)

def plot_cdf(nums, ax, title):
    nums_sorted = np.sort(nums)
    cdf = np.arange(1, len(nums_sorted) + 1) / len(nums_sorted)
    ax.plot(nums_sorted, cdf, marker=".", linestyle="none")
    ax.set_title(title)
    ax.set_xlabel('Value')
    ax.set_ylabel('Cumulative Probability')
    ax.grid(True)

# Create subplots for the CDFs
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Plot each CDF
plot_cdf(exponential_RV, axes[0], 'CDF of Exponential Distribution')
plot_cdf(pareto_RV, axes[1], 'CDF of Pareto Distribution')
plot_cdf(gaussian_RV, axes[2], 'CDF of Gaussian Distribution')

plt.tight_layout()
plt.show()
