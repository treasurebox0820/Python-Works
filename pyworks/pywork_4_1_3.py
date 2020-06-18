"""
2. 上記のファイルの先頭５行のみを表示するプログラムを
実行に時間がかからない方法で作成してください

3. 上記ファイルの先頭20行のデータを読み込んで、ユーザーID順、身長順、
体重の順に並び替えて表示してください。

4. 上記ファイルの１万件全てのデータから身長と体重の
最小値、最大値、平均値を計算して表示してください。

sortとsortedの違い
sort:返り値はNone. 今回の場合だとlist_userを勝手に書き換える
sorted:返り値がリストになっている。勝手に書き換えない

list_user.sort(key = lambda x:x[1])
csv.path

"""

k = 0
list_user = []
with open("sample3.txt","r") as f:
    for i in f :
        if k == 20:
            break

        y = i.replace("cm","")
        z = y.replace("kg","")
        one_list = z.split(",")
        list_user.append(one_list)
        k += 1

#○○順に並べたリストを作る

sorted_by_weight_list = sorted(list_user, key = lambda x:x[1])
sorted_by_height_list = sorted(list_user, key = lambda x:x[2])

#入れたリストを順番に表示する関数
def show_in_specific_order(some_list):
    """
    入れたリストを○○順番に表示する関数
    引数＝リスト
    """
    for i in range(0,20):
        print(some_list[i])


print("体重順")
show_in_specific_order(sorted_by_weight_list)
print("身長順")
show_in_specific_order(sorted_by_height_list)
    

def get_maximum_height():

