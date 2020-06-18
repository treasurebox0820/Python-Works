"""
1.標準ライブラリの turtle モジュールの Turtle クラスを継承して亀が図形を描くためのクラスを作成します。次の手順で理解しながら進めてください。
　1.turtle モジュールをインポートして、Turtle クラスのインスタンス t1 を生成し、下記のメソッドを試してください。（その他のメソッドは dir(), help() で調べること）
　　1.線を描く　t1.pendown(), t1.forward(150), t1.penup()
　　2.向きを変える　t.left(90), t1.right(60)
　　3.カーソルを亀の形に変える　t1.shape("turtle"), t1.shapesize(2, 2, 3)
　　4.円を描く　t1.circle(150)
　　5.キャンバスをクリア、ホームに戻る　t1.clear(),  t1.home()
　　6.キャンバスの大きさ　t1.getscreen().window_width(), t1.getscreen().window_height()
　　7.カーソルの座標を得る、指定された座標へ行く　t1.position(), t1.goto(x, y)
 （ヒント）プログラムの途中や最後に _empty = input("Enterで次へ") を書いておくと Window を閉じずに保持できます。
　2.上記を応用して正三角形を描画する関数を作成してください。
　3.turtle モジュールの Turtle クラスを継承して Kame というクラスを作成してください。
ただし、Kame クラスでインスタンスを生成すると、最初から大きい亀の形をしたカーソルが表示されるようにクラスを作成してください。
　4.Kame クラスに 正三角形を描くメソッドを追加してください。
　5.Kame クラスに正四角形と正六角形を描くメソッドを追加してください。
　6.Kame クラスに正n角形(nは自然数)を描くメソッドを追加して、正七角形を描いてください。
　7.（時間が余ったら）亀を使ってなにかご自分が美しいと思うものを描いてください。
"""
from turtle import Turtle
x=0
y=0
t1 = Turtle()
t1.pendown()
t1.forward(60)


#向きを変える
t1.left(90)
t1.right(60)

#カーソルをカメの形に変える
t1.shape("turtle"),t1.shapesize(2,2,8)

#キャンパスをクリア
#t1.clear()
#t1.home()

#キャンバスの大きさ

t2 = Turtle()
t2.getscreen().bgcolor("pink")

"""
.window_width(2000),
t1.getscreen().window_height(2000)
"""

print(t1.position())
print(t1.goto(x, y))

_empty = input("Enterで次へ")