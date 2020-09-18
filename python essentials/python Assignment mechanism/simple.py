x=500
print(id(x))
y=x
print(id(y))
a=x is y
print(a)

y='yeal'
print(id(y))
print(x is y)

b=2
print(id(b))
c=2
print(id(c))
print(b is c)