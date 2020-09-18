"""元组用（）来生成
   元组数据不可变，会报错
"""

t=(10,11,12,13)
print(t)
print(t[0])
"""索引切片"""
print(t[1:3])

"""由于`()`在表达式中被应用，只含有单个元素的元组容易和表达式混淆，所以采用下列方式定义只有一个元素的元组："""
a=(10,)
print(a)
print(type(a)) #此处为tuple类型
b=(10)
print(b)
print(type(b))  #此处为int类型

"""为什么此处的c没有变化？？？"""
c=[10,11,12,13]
tuple(c)
print(c)
print(tuple(c))
"""计算元组的个数和位置"""
x=(1,2,3,4,6,6,7,8,9)
print(x.count(6))
print(x.index(9))