n = input("数字を入力 > ")
try:
   print(1 / int(n))
except:
   print("全ての例外")
else:
   print("正常終了時")
finally:
   print("終了時")