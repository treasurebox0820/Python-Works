"""
クロージャーとは何か？
"""
def make_circle_area_func(pi=3.14):
   """円の面積を計算する関数を作る"""
   def circle_area(radius):
       """円の面積を計算する"""
       return radius * radius * pi
   return circle_area
if __name__ == "__main__":
   circle_area_default = make_circle_area_func() # pi=3.14
   circle_area_precise = make_circle_area_func(pi=3.1415926535)
   print(circle_area_default(2))  # pi=3.14  の場合の計算
   print(circle_area_precise(2))  # pi=3.1415926535 の計算