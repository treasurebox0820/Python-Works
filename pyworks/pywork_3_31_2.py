"""
機能を追加したい時に使うのがデコレーター
"""
def show_how_it_works(func):
   """引数と戻り値を表示するデコレータ"""
   #myfuncitionはwrapperとかか
   def myfunction(*args, **kwargs):
       """関数の引数と戻り値を表示する"""
       #加える機能３つ、以下の三行
       print('Running function:', func.__name__)
       print('Positional arguments:', args)
       print('Keyword argments:', kwargs)
       result = func(*args, **kwargs)
       print('Result:', result)
       return result
   return myfunction
if __name__ == "__main__":
   def add_two_numbers(a, b):
       return a + b
   decolated_func = show_how_it_works(add_two_numbers)
   decolated_func(1, 8)
