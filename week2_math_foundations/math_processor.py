# Experimental engineering data metrics
data = [85.5, 90.0, 78.2, 92.5, 88.1, 79.4, 95.0, 83.3]

# 1. Calculate the Mean (Average) using a loop
total_sum = 0
for value in data:
    total_sum += value

mean = total_sum / len(data)
print(f"Calculated Mean: {mean:.2f}")

# 2. YOUR TASK: Calculate the Variance using your math background
# Formula: Variance = (1/N) * sum((x - mean)**2)

variance_sum = 0
for value in data:
    # In Python, exponents/powers use '**' instead of '^'
    # So (x - mean)^2 is written as: (value - mean) ** 2
    variance_sum += (value - mean) ** 2

variance = variance_sum / len(data)
print(f"Calculated Variance: {variance:.2f}")