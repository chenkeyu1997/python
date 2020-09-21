"""分片用来从序列中提取出想要的子序列，其用法为：
var[lower:upper:step]
其范围包括 lower ，但不包括 upper ，即 [lower, upper)， step 表示取值间隔大小，如果没有默认为1。
"""

s="hello world"
print(s[1:3])
print(s[1:-2])
print(s[:3])
print(s[:])
print(s[::2])