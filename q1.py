modulus = 2**32
def rng(seed):
    a = 1664525
    b = 1013904223  
    nextSeed =( (a*seed)+b ) % modulus
    return nextSeed / modulus

seed = 33 
n = 10
nums = [];
for _ in range(n):
    nums.append(rng(seed))
    seed = rng(seed) * modulus

print(nums)
