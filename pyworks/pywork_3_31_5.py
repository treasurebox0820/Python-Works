"""
組み込み関数 filter を使って、1から20までの整数のリストから奇数のみを取り出して繰り返し処理を作り、
値を表示しながら合計値を計算して結果を表示してください。（ヒント: lambda式を使うこともできます）

疑問
filterはどういう時に使うの？
filterはiterable の要素のうち function が真を返すものでイテレータを構築します。

filterが返すのはイテレーター型
listを二回使うと一回目でポインターが最後まで行ってしまう

ジェネレーター、反復子を作る仕組み

"""
x = 0
for e in filter(lambda i: i%2 !=0,range(1,21)):
    x += e
    print(e)
print(f"合計値は{x}",)