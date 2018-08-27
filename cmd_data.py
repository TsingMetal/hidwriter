# 读取计数器信息
counter_cmd = [0x01] + [0x00] * 63

# 写入计数器数值
init_count_cmd = [0x02, 0x01] + [0x09] * 4 + [0x00] * 58

# 写入计数器治具编号
init_fixture_id_cmd = [0x02] * 2 + [0x09] * 30 + [0x00] * 32

# 写入上次治具保养时间
init_Maintenance_time_cmd = [0x02, 0x03] + [0x08] * 6 + [0x00] * 56

# 写入上次治具保养时次数
init_Maintenance_count_cmd = [0x02, 0x04] + [0x09] * 6 + [0x00] * 56

# 写入治具保养次数限制
init_count_limit_cmd = [0x02, 0x05] + [0x09] * 6 + [0x00] * 56
