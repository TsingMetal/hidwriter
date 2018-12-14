#_*_coding: utf-8_*_


# 读取计数器信息
prefix = [0x00, 0x1f]
postfix = [0x0d]
temp = [0x00] * 29
COUNTER_CMD = prefix + [0x11] + temp + postfix

# 写入计数器数值
INIT_COUNT_CMD = prefix + [0x21] + [0x00] * 29 + postfix

# 写入计数器治具编号
INIT_FIXTURE_ID_CMD = [0x00, 0x1f] + [0x22] * 2 + [0x00] * 62

# 写入上次治具保养时间
INIT_MAINTENANCE_TIME_CMD = [0x00, 0x1f, 0x23, 0x03] + [0x00] * 62

# 写入上次治具保养时次数
INIT_MAINTENANCE_COUNT_CMD = [0x00, 0x1f, 0x24, 0x04] + [0x00] * 62

# 写入治具保养次数限制
INIT_COUNT_LIMIT_CMD = [0x00, 0x1f, 0x25, 0x25] + [0x00] * 62
