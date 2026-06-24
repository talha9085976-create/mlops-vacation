import numpy as np
import time

# Create a massive dataset of 1,000,000 random engineering metrics
large_dataset = np.random.randn(1000000)

print("--- Processing 1 Million Data Points ---")

# Method A: Traditional Loop Method
start_loop = time.time()
total_sum = 0
for value in large_dataset:
    total_sum += value
loop_mean = total_sum / len(large_dataset)
end_loop = time.time() - start_loop
print(f"Loop calculated mean: {loop_mean:.4f} in {end_loop:.5f} seconds")

# Method B: Vectorized NumPy Method (No Loops!)
start_numpy = time.time()
numpy_mean = np.mean(large_dataset)  # Done in a single execution step
end_numpy = time.time() - start_numpy
print(f"NumPy calculated mean: {numpy_mean:.4f} in {end_numpy:.5f} seconds")

# Calculate how much faster NumPy processed the matrix
speed_multiplier = end_loop / end_numpy
print(f"\n🚀 Vectorization is roughly {speed_multiplier:.1f}x FASTER than a loop!")
