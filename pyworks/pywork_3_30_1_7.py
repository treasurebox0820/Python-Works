"""
3.turtle モジュールの Turtle クラスを継承して Kame というクラスを作成してください。
ただし、Kame クラスでインスタンスを生成すると、
最初から大きい亀の形をしたカーソルが表示されるようにクラスを作成してください。

4.Kame クラスに 正三角形を描くメソッドを追加してください。

5.Kame クラスに正四角形と正六角形を描くメソッドを追加してください。

6.Kame クラスに正n角形(nは自然数)を描くメソッドを追加して、正七角形を描いてください。

わかったこと＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
selfでなくてt1のようなインスタンスをクラス内で生成した場合にはカメは一緒に動かない

"""
from turtle import Turtle

class Kame(Turtle):

    """
    """
    def __init__(self):
        """
        """
        super().__init__()

        self.shape("turtle")
        self.shapesize(2,2,8)
        self.speed("fastest")
        self.np = 3

    def draw_traiangle(self):
        """
        三角形を描く関数
        """
        self.pendown()
        i = 0
        while i<3:
            self.forward(200)
            self.left(120)
            i += 1
        self.penup()
    def draw_square(self):
        """
        正方形を描く関数
        """
        self.pendown()
        i = 0
        while i < 4:
            self.forward(200)
            self.left(90)
            i += 1
        self.penup()
    def draw_hexagon(self):
        self.pendown()
        i = 0
        while i <6:
            self.forward(150)
            self.left(60)
            i += 1
        self.penup()
    def draw_shape(self):
        """
        n角形を描く関数
        """        
        self.pendown()
        k.np = 20
        i = 0
        #nは今回７角形で
        while i <self.np:
            self.forward(15)
            self.left(180-((180*(self.np-2))/self.np))
            i += 1
        self.penup()

if __name__ == "__main__":
    k = Kame()
 
    k.draw_shape()
    #k.getscreen().window_width()
    _empty = input("Enterで次へ")
#t1.getscreen().window_width(), t1.getscreen().window_height()