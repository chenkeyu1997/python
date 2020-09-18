"""整型和字符串是字典常用的类型，浮点型不推荐(精度影响）"""
data={}
data[1.1+2.2]=6.6
# print(data[3.3])
print(data)  #{3.3000000000000003: 6.6}

"""用get方法创建字典"""
a={}
a["one"]="this is number 1"
a["two"]="this is number 2"
a.get("three","undefined")
print(a.get("three","undefined"))

print(a.pop("two"))
print(a)

del a["one"]
print(a)
