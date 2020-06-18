"""
    def while_method(self,x):

        while文を勝手にやってくれるメソッド

        while i < x:
            self.pendown()
            self.forward(50)
            self
"""

import random
from pywork_3_30_1_7 import Kame
class Art(Kame):
    """
    美しいものを生成するクラス。
    """
    def __init__(self):
        """
        初期メソッド
        """
        super().__init__()
        self.speed("fast")
        #npはnumber polygonです。初期値３
        self.np = 3       

    def draw_shape2(self):
        super().draw_shape()
        """
        左回りに多正角形を生成するメソッド
        """
        i = 0
        while i <self.np:
            self.pendown()
            self.forward(100)
            self.right(180-((180*(self.np-2))/self.np))
            i += 1
    def draw_shape3(self,weird):
        i = 0
        while i <self.np:
            self.pendown()
            self.forward(100)
            self.right(weird-((180*(self.np-2))/self.np))
            i += 1

if __name__ == "__main__":
#art型のインスタンスを二つ生成
    k1 = Art()
    k2 = Art()
    k3 = Art()
    k1.pen(pencolor="blue")
    k2.pen(pencolor="red")
    k3.pen(pencolor="green")

    for i in range(30):
        list_which = [k1.draw_shape(),k2.draw_shape2(),k3.draw_shape3(random.randrange(1,30))]
    _empty = input("Enterで次へ")

    #疑問、変数にいれた