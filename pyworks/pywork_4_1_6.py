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
　3.提供される予定の関数 month を利用して、
１年分のカレンダーを文字列として出力する関数 show_year_cal を作成してください。
カレンダーは ３列4行に並べる場合をデフォルトとして、そのほか、
任意の並び順に対応させてください。
関数 show_year_cal の第一引数は西暦年を表す数値としてください。
　4.１ヶ月分のカレンダーのフォーマットの要件を満たす疑似データを作成し、
それを使ってshow_year_cal の機能の確認テストを行ってください。
　5.この課題が終わった人は講師に連絡ください。１の機能を持つ関数を提供しますので、それを使って来年のカレンダーを標準出力に表示するプログラムを完成させてください。
　6.（時間が余ったら）英語名で表示されている部分を日本語名に置き換えて表示してください。
（標準取組時間: 3時間、 5番まで） 

１年分のカレンダーを文字列として出力する関数 show_year_cal を作成してください。
カレンダーは ３列4行に並べる場合をデフォルトとして、そのほか、
任意の並び順に対応させてください。
関数 show_year_cal の第一引数は西暦年を表す数値としてください。

"""
import calendar
def make_year_calendar(year,month):
    """
    show_year_calendarが正常に動くかを検証する関数
    """
    test = """
{}    {}
montuewedthufrisatsun  
1  2  3  4  5  6  7
8  9  10 11 12 13 14
15 16 17 18 19 20 21
20 21 22 23 24 25 26
27 28 29 30 31 32 33
34
""".format(year,month)
    return test
    

def show_year_calendar(n):
    """
    month関数からもらったカレンダー情報を表示する関数
    """   
    for i in range(0,int(12/n)):
        for k in range(8):
            str_ = ""
            for j in range (1,n+1):
                if 12 % n != 0:
                    break
                new_list = calendar.month(2020,int(j+i*n)).strip().splitlines()
                new_list.append("")
                str_ += "{:25}".format(new_list[k])
            print(str_)            
        print("\n")

if __name__ == "__main__"
show_year_calendar(4)




    



















"""
list_3_4 =[[test for i in range(1)] for j in range (2)]
#print(list_3_4)

print(f"{test},      {test},{test}",end="")
print(f"{test},      {test},{test}",end="")
print({1:test,2:test,3:test})
I = 4
J = 12/4
list_3_4 =[[2 for i in range(I-1)] for j in range (J-1)]
pass
"""