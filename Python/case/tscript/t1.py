import struct

# 目标和
target = 0xDEADBEEF

# 前三个 dword，选可打印 ASCII 字符
d0 = 0x41414141  # "AAAA"
d1 = 0x42424242  # "BBBB"
d2 = 0x43434343  # "CCCC"

# 计算第四个 dword
d3 = (target - (d0 + d1 + d2)) & 0xFFFFFFFF

# 拼接成16字节 key
key = struct.pack('<I', d0) + struct.pack('<I', d1) + struct.pack('<I', d2) + struct.pack('<I', d3)

# 输出可见字符
print("Key bytes:", key)
print("Key hex:", key.hex())