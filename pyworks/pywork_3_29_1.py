"""
【ワーク 4-3：関数とモジュール】
1.来年のカレンダーを標準出力に表示するプログラムを下記のように作成します。
　1.引数に西暦年と月を入力すると、１ヶ月分のフォーマット済みのカレンダーを文字列として出力する関数
 month が提供される（誰かが作ってくれる）と仮定します。
 第１引数が年(整数)、第2引数が月(整数)です。戻り値は１ヶ月分のカレンダーを表す文字列です。
　2.１ヶ月分のカレンダーのフォーマットの仕様は下記です。
　　1.表示範囲は半角文字７行20列、ただし月の最後の日付の直後は改行。
　　2.１行目が月と年(英語名)、
　　3.２行目が曜日ラベル(英語名)。
　3.提供される予定の関数 month を利用して、１年分のカレンダーを文字列として出力する関数
 show_year_cal を作成してください。
カレンダーは ３列4行に並べる場合をデフォルトとして、そのほか、
任意の並び順に対応させてください。関数 show_year_cal の第一引数は西暦年を表す数値としてください。
　4.１ヶ月分のカレンダーのフォーマットの要件を満たす疑似データを作成し、
それを使ってshow_year_cal の機能の確認テストを行ってください。
　5.この課題が終わった人は講師に連絡ください。１の機能を持つ関数を提供しますので、それを使って来年のカレンダーを標準出力に表示するプログラムを完成させてください。
　6.（時間が余ったら）英語名で表示されている部分を日本語名に置き換えて表示してください。
"""

from pywork_3_29_1_2 import month
year = 2020
def type_of_calendar():
    """
    カレンダーの表示の仕方を決定する関数
    """
   
    while True:
        input_format = input("表示方法を選択してください。\n1.2×6\n2.3×4\n3.4×3\n")
        if input_format == "1":
            return 2
        elif input_format == "2":
            return 3
        elif input_format == "3":
            return 4
        elif input_format == "4":
            return 6
        else: print("必ず表示された方法を選択してください")

#def show_year_cal(x)
 #   print()


"""
def show_year_cal(x):

    dic_1st = {}
    dic_2nd = {}
    dic_3rd = {}
    dic_4th = {}
    dic_5th = {}
    dic_6th = {}
    dic_calendar = {}
    if x == "type_2_6":
        i = 1
        while i <= 12:
        #カレンダーの一列目の辞書dict_1st
            if i <= 2:
                dic_1st[i] = year
            elif i <= 4:
                dic_2nd[i] = year
            elif i <= 6:
                dic_3rd[i] = year
            elif i <= 8:
                dic_4th[i] = year
            elif i <= 10:
                dic_5th[i] = year
            elif i <= 12:
                dic_6th[i] = year
            i += 1
        print(dic_6th)
"""  


if __name__ == "__main__":
    list[]
    for i in range(1,13):
        for i2 in range (1,8)
            list_test[i] = month(i).split("\n")
            print(list_test)

#    show_year_cal(type_of_calendar())
#    print(dic_6th)