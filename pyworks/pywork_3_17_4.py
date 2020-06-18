"""
問題\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
リスト ["Beautiful", "is", "better", "than", "ugly"] の中身を要素でアクセスして、
先頭と最後の部分を上書きすることにより ["Explicit", "is", "better", "than", "implicit"] に書き換えてください。

これを言い換えると、
中身を要素でアクセスする⇔リストの中身を文字列によってアクセスする⇔その言葉が入ってたら、
他の言葉と入れ替える
だから、


"""
list= ["Beautiful", "is", "better", "than", "ugly"]

print(list)
if list[0]=="Beautiful":
    list[0]="Explicit"
elif list[1]=="Beautiful":
    list[1]="Explicit"
elif list[2]=="Beautiful":
    list[2]="Explicit"
elif list[3]=="Beautiful":
    list[3]="Explicit"
elif list[4]=="Beautiful":
    list[4]="Explicit"

if list[0]=="ugly":
    list[0]="implicit"
elif list[1]=="ugly":
    list[1]="implicit"
elif list[2]=="ugly":
    list[2]="implicit"
elif list[3]=="ugly":
    list[3]="implicit"
elif list[4]=="ugly":
    list[4]="implicit"

print(list)