"""
2.成績管理表のクラスを作る
　1.中学生の名前と３教科（国語、数学、英語）の成績を属性にもつクラス（型）を作成し、
5人分のインスタンスを作成してください。
　2.random モジュールを使って、任意の名前と成績を 100 人分生成してファイルに保存してください。
"""

class Grade():
    """
    """
    classname = "一組"

    def __init__(self,name,japanese ,english, math):
        self.name = name
        self.japanese = japanese
        self.english = english
        self.math = math

#インスタンスを５人分生成
taro = Grade("太郎",32,34,39)
ito = Grade("伊藤",98 ,12, 74)
kon = Grade("懇",58 ,72, 34)
zen = Grade("善",68 ,12, 34)
yama = Grade("山",43, 80, 39)

print(type(taro))
print(taro.name)
