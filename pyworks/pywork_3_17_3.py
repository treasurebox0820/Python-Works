sent=input("文章を打ってください")

str=[]
str.append(sent)
#sentは文字型の変数だからリストにいれられないのかチェック。
print(str)

if "地名" in str or "占い" in str or "時刻" in str:
    print("回答します。")
else:
    print (sent)
