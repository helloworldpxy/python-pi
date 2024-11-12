import mpmath
import pandas as pd

def calculate_pi(digits):
    """ 使用mpmath库计算指定位数的圆周率 """
    mpmath.mp.dps = digits  # 设置小数点后位数
    return str(mpmath.mp.pi)

# 设置要计算的圆周率的位数
precision = 100  # 例如，100位

try:
    # 计算一次圆周率即可，因为每次计算结果相同
    pi_str = calculate_pi(precision)
    
    # 创建一个DataFrame来存储结果
    results = pd.DataFrame({
        'Run': range(1, 101),
        'Pi_Value': [pi_str] * 100
    })

    # 将结果写入Excel文件
    output_file = 'pi_results.xlsx'
    results.to_excel(output_file, index=False)

    print(f"圆周率计算结果已写入到{output_file}")
except Exception as e:
    print(f"发生错误: {e}")
