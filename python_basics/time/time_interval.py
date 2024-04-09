from datetime import datetime

# 给定的datetime
given_datetime = datetime(2023, 9, 19, 23, 0, 0)  # 替换为你的给定datetime

# 获取当前时间
current_datetime = datetime.now()

# 计算时间差
time_difference = current_datetime - given_datetime

# 将时间差转换为分钟
minutes_difference = time_difference.total_seconds() / 60

# 输出时间差（分钟）
print("时间差（分钟）:", minutes_difference)
