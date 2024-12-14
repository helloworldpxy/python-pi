import threading
import random
import time

def calculate_pi(thread_id, points_per_thread, result):
    # 计算单个线程内落在单位圆内的点数
    inside_circle = 0
    try:
        for _ in range(points_per_thread):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            if x**2 + y**2 <= 1:
                inside_circle += 1
        result[thread_id] = inside_circle
    except Exception as e:
        print(f"线程 {thread_id} 出现错误: {e}")

def main(total_points, num_threads):
    # 主函数，使用多线程计算圆周率
    if num_threads <= 0:
        raise ValueError("线程数必须大于0")
    if total_points <= 0:
        raise ValueError("总点数必须大于0")

    threads = []
    result = [0] * num_threads
    points_per_thread = total_points // num_threads
    # 如果无法整除，最后一个线程计算剩余的点数
    last_thread_points = total_points - points_per_thread * (num_threads - 1)

    start_time = time.time()

    for i in range(num_threads):
        thread_points = points_per_thread if i != num_threads - 1 else last_thread_points
        thread = threading.Thread(target=calculate_pi, args=(i, thread_points, result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    inside_circle = sum(result)
    pi_estimate = (inside_circle / total_points) * 4

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"计算结果: {pi_estimate}")
    print(f"程序运行总时间: {elapsed_time:.5f} 秒")

if __name__ == "__main__":
    # 程序入口，获取用户输入并调用主函数
    try:
        total_points = int(input("请输入计算圆周率所需的总点数: "))
        num_threads = int(input("请输入使用的线程数: "))
        main(total_points, num_threads)
    except ValueError as ve:
        print(f"输入错误: {ve}")
    except Exception as e:
        print(f"程序运行出现错误: {e}")
