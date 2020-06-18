"""


問題｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜
次のようなプログラムを作成してください。
　1.「キーを入力してください」と表示して値を入力させる。
　2.「バリューを入力してください」と表示して値を入力させる。
　3.入力結果を辞書 dict に記録していく。
　4.辞書を表示する。
　5.1に戻る、
　6.途中で「exit」と入力されたら終了する。""
問題｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜｜
起こったエラー＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠
TypeError: list indices must be integers or slices, not str

IndexError: list assignment index out of range
間違えてリスト型で作ってた。
制作手順＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠
先にlist_を空で作っておく。
-1:key_とvalue_がexitになった瞬間に終わるようにする
１、２：インプット文でkey_とvalue_を入力させる
３：list_にkey_とvalue_を代入する
４：print文でlist_を表示する
"""
dict_={}
while True:
    key_=input("欲しい要素の”値を入力せよ＞")
    value_=input("欲しい要素の”キーを入力せよ＞")
    if key_=="exit" or value_=="exit": 
        break
    else:
        dict_[key_]=value_
        print(dict_)
