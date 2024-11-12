import mpmath
import pandas as pd

def calculate_pi(digits):
    """ 使用mpmath库计算指定位数的圆周率 """
    mpmath.mp.dps = digits  # 设置小数点后位数
    pi_value = mpmath.mp.pi
    return pi_value

# 设置要计算的圆周率的位数
precision = 100  # 例如，100位

# 创建一个DataFrame来存储结果
results = pd.DataFrame(columns=['Run', 'Pi_Value'])

# 重复运行100次
for i in range(1, 101):
    pi_value = calculate_pi(precision)
    # 由于mpmath的pi是一个高精度浮点数，我们将其转换为字符串以保存
    pi_str = str(pi_value)[:precision+2]  # 保留足够的位数加上小数点
    results = results._append({'Run': i, 'Pi_Value': pi_str}, ignore_index=True)

# 将结果写入Excel文件
output_file = 'pi_results.xlsx'
results.to_excel(output_file, index=False)

print(f"圆周率计算结果已写入到{output_file}")