"""
問題
与えられた整数が偶数かどうかを判定する関数 is_even を作ってください。
それを使って、1から6までの数字の偶奇を判定して表示してください。

与えられた整数が引数かどうか判定する関数
1.関数を定義する
2.１から６までの数字の偶奇を判定してください
3.


藤岡さん発表
計算する部分と表示する部分を分けておく。
"""
def is_even(integer):
    """
    与えられた引数の値が偶数か引数かを判断する関数です。
    """
    try:
        judge_int = int(integer)
    except ValueError as e:
        print("整数ではない値が入力されました。")
        print(e)
    except:
        print("入力エラー以外のエラーが発生しました。")
    if judge_int % 2 == 0:
        return True
    else:
        return False


if __name__ ==""__main__":
for i in range(1,7):
    if is_even(i):
        print(i,"は偶数です")
    else:
        print(i,"は奇数です")

