"""
リスト ["Beautiful", "is", "better", "than", "ugly"] の中身を要素でアクセスして、
先頭と最後の部分を上書きすることにより ["Explicit", "is", "better", "than", "implicit"] に書き換えてください。

これを言い換えると、
中身を要素でアクセスする⇔リストの中身を文字列によってアクセスする⇔その言葉が入ってたら、
他の言葉と入れ替える。
"""

list= ["Beautiful", "is", "better", "than", "ugly"]
for i in range(5):
    if list[i]=="Beautiful":
        list[i]="Explicit"
    if list[i]=="ugly":
        list[i]="implicit"
print(list)

x = ""
for i in list:
    x += i+" "
x += "."
print(x)