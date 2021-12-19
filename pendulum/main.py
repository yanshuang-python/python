import pendulum as pu
# 相差多少小时(计算昨天和明天)

# 获取昨天时间
d1 = pu.yesterday()
# 获取明天时间
d2 = pu.tomorrow()
print(d1.diff(d2).in_hours())
