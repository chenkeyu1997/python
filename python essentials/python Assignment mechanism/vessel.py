x=[500,501,502]
print(id(x[0]))
print(id(x[1]))
print(id(x[2]))
print(id(x))

y=x
print(id(y))

y[1]=600
print(id(y))
print(id(x[1]))
print(id(y[1]))

y=[700,800]
print(id(y))
print(id(x))

print(id(x[1]))
print(id(y[1]))

