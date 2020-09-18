def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

if __name__ == '__main__':   #调用函数
    print(fib(5))