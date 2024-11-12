import mpmath

def calculate_pi(digits):
    # 使用mpmath库计算指定位数的圆周率
    mpmath.mp.dps = digits  # 设置小数点后位数
    pi_value = mpmath.mp.pi
    return pi_value

# 设置要计算的圆周率的位数
precision = 1000000

pi_value = calculate_pi(precision)
print(f"计算结果为{pi_value}")