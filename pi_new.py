import random

def calculate_pi(num_samples):
    try:
        inside_circle = sum(1 for _ in range(num_samples) if random.uniform(-1, 1)**2 + random.uniform(-1, 1)**2 <= 1)
        return 4 * inside_circle / num_samples
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# 设置模拟次数
num_samples = 100000
pi_estimate = calculate_pi(num_samples)
if pi_estimate is not None:
    print(f"Estimated π using {num_samples} samples: {pi_estimate}")
else:
    print("Failed to estimate π due to an error.")
