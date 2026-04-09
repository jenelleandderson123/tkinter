import numpy as np

numbers = input("Enter numbers separated by spaces: ").split()
numbers = np.array([float(num) for num in numbers])

print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Median:", np.median(numbers))
print("Standard Deviation:", np.std(numbers))