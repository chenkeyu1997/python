#w会覆盖之前所写内容
f=open('test.txt','w')
f.write('hello man!')
f.close()
print(open('test.txt').read())

#a不会覆盖之前内容
f = open('test.txt', 'a')
f.write('... and more')
f.close()
print(open('test.txt').read())

