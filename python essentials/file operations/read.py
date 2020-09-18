f=open("test.txt","r")
line=f.read()
print(line)
f.close()
"""
read()
readline() 一次读取一行；
readlined()  :一次读全部；

"""

f = open('123.txt')
for line in f:
    print(line)
f.close()

#移除文件
import os
os.remove('test.txt')