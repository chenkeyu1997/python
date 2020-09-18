#字典的数据类型
a={}
print(type(a))

a["one"]="this is number 1"
a["two"]="this is number 2"
print(a)

print(a['one'])

a["one"]="this is number 1,yeal"
print(a)


b={'one':'this is apple','two':'this is banana'}
print(b['one'])

#用dict初始化字典
inventory=dict([('a',123),('b',456),('c',789)])
print(inventory)
inventory['a']+=1
print(inventory)