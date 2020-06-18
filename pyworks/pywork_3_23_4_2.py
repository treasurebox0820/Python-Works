"""
3（時間が余ったら）２の課題は①while の条件式で終了条件にする方法と、
②無限ループを作成しておき途中に if 文を挿入して break で抜ける方法、があります。
①か②のうちまだ使っていないもう一方の方法で作成してください。
制作手順
whileの条件式に


"""

#aが足されていく変数。add入力されては足される変数
a=0
add="0"
while add.isnumeric() or add!="exit":
    add = input("足したい数を入力してね")
    if add.isnumeric():
        a=a+float(add)
print(a)





"""
a=0
add="0"
while add.isnumeric()==True:
    add = input("足したい数を入力してね")
    if add=="exit":
        break
    if float(add)>-999999999:
        a=a+float(add)
print(a)
"""



"""
先にexitの方を先頭にした意味はあるのか？

"""