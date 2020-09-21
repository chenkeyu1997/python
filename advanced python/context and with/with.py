with open('my_file', 'w') as fp:
    data=fp.write("Hello world")
"""此代码等效于下面代码
fp=open('my_file','w')
try:
    data=fp.write("Hello world")
finally:
    fp.close()

其基本用法如下：

with <expression>:
    <block>
<expression> 执行的结果应当返回一个实现了上下文管理器的对象，即实现这样两个方法，__enter__ 和 __exit__：
"""
class ContextManager(object):
    def __enter__(self):
        print("Entering")
    def __exit__(self, exc_type, exc_val, traceback):
        print("Exiting")

with ContextManager():
    print("Inside the with statement")
    print(1/0)