"""
問題
数値を要素とするリストを受け取り平均値を計算する関数 calc_ave を作ってください。
それを使って、次に与えるリストの平均値を計算してください。リスト：[40, 61, 52, 38, 45]

藤岡さん発表


"""


def calc_ave(list_):
    """
    数値を要素とするリストを受け取り平均値を計算する関数 
    仮引数：list_
    変数：number:要素の個数
        : total:すべての要素の合計
    """
    number = len(list_)
    total = sum(list_)
    average = total/number

    return average
#計算したいリスト
list_=[40, 61, 52, 38, 45]

#平均の表示
print("リスト{}の平均は{}".format(list_,calc_ave(list_)))