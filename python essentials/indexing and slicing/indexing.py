s='hello world'
print(s[0])
"""负向索引，负几则表示倒数第几个元素"""
print(s[-2])
try:
    print(s[123])
except IndexError:
    print("string index out of range")

