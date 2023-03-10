def estimate_statistics(nums):
    n = len(nums)
    mean = sum(nums) / n
    variance = sum((x - mean) ** 2 for x in nums) / (n - 1)
    std_dev = variance ** 0.5
    return mean, variance, std_dev

# Example usage
numbers = [1, 2, 3, 4, 5]
mean, variance, std_dev = estimate_statistics(numbers)
print(f"Mean: {mean:.2f}")
print(f"Variance: {variance:.2f}")
print(f"Standard deviation: {std_dev:.2f}")
