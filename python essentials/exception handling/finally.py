try:
    print(1/0)
except ZeroDivisionError:
    print("division by zero")
finally:
    print("finall is called")
