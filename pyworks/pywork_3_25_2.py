n = input("数字を入力 > ")
my_list = [1, 2, 3]
my_dict = {0:"Tokyo", 1:"Osaka"}
try:
   i_n = int(n)
   print("割り算     :", 1 / i_n)
   print("リストの要素:", my_list[i_n])
   print("辞書のキー :", my_dict[i_n])
except ZeroDivisionError as e:
   print("Z:", type(e), e)
except ValueError as e:
   print("V:", type(e), e)
except (IndexError, KeyError) as e:
   print("I or K:", type(e), e)
except:
   print("そのほかの例外")