"""
3.(時間があったら)２の課題で２つの辞書ファイルを作成し、
読み込む際には辞書を選んで切り替えられるようにしてください。
"""


while True:
    select = input("辞書１？辞書２？")
    if select=="辞書１" or select =="辞書２":
        break

word="犬\nいぬ\n猫\nねこ\n狐\nきつね\n"
with open("sample.txt","a",encoding="utf_8_sig") as f:
	f.write(word)
with open("sample.txt","r",encoding="utf_8_sig") as f:  
    data=f.readlines()
    for i in range(len(data)):
        data[i] = data[i].replace("\n"," ")
if select=="辞書１":
    dict_1={data[0]:data[1],data[2]:data[3],data[4]:data[5]}
    print("これは辞書１です。　",dict_1)
else:
    dict_2={data[0]:data[1],data[2]:data[3],data[4]:data[5]}
    print("これは辞書２です。 ",dict_2)
