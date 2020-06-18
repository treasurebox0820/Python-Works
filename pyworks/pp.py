"""
検証自分でやったワーク
initの引数と初期メソッドの中で定義するインスタンスはどうちがうのか？
以下の文は実は書かなくてもよい。訂正。かかないとアトリビュートができないからかかないといけない。
self.width = width
self.height = height
self.depth = depth
"""
class Prism:
    def __init__(self, width=2, height=3, depth=4):
        self.width = width
        self.height = height
        self.depth = depth

a = Prism(234,432,999)
a.width = "a"
b = Prism()
print(a.width)
print(a.height)
print(a.depth)

print(b.width)
print(b.height)
print(b.depth)
