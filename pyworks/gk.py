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
