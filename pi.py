import random

def calculate_pi(num_samples):
    inside_circle = 0
    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        # 检查点(x, y)是否在单位圆内
        if x**2 + y**2 <= 1:
            inside_circle += 1
    # 根据蒙特卡洛方法的原理，π ≈ 4 * (圆内点数 / 总点数)
    pi_estimate = 4 * inside_circle / num_samples
    return pi_estimate

# 设置模拟次数
num_samples = 100000
pi_estimate = calculate_pi(num_samples)
print(f"Estimated π using {num_samples} samples: {pi_estimate}")