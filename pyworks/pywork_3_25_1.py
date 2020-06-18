n =input("数字を入力＞")
try:
    print(1/float(n))
except ZeroDivisionError as e:
    print(e)
    print(type(e))