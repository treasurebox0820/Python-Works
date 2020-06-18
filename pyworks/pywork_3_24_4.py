"""
問題＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠
1.「辞書(dict) と 繰り返し処理 & ファイル入出力」のワークAの続きです。
下記の要件を満たすようにプログラムを更新してください。
•ファイルの保存先をカレントディレクトリの下の dicfiles というディレクトリにしてください。
•dicfiles というディレクトリがなければ新規作成してください。
•保存するファイルが存在しない場合は新規作成し、ある場合は、新しいデータのみを追加してください。

os, listdir()
以下の一番か二番からしか


if not

strip
pathlib()
引数がないと今実行されてるアドレスを表示
pathlib.Path("")
p.exist
dir=resolve()
mkdir(dir)

"""

while True:
    select = input("辞書１？辞書２？")
    if select=="辞書１" or select =="辞書２":
        break

word="犬\nいぬ\n猫\nねこ\n狐\nきつね\n"
with open("C:\\pyworks\\dicfiles\\sample.txt","w",encoding="utf_8_sig") as f:
	f.write(word)
with open("C:\\pyworks\\dicfiles\\sample.txt","r",encoding="utf_8_sig") as f:  
    data=f.readlines()
    for i in range(len(data)):
        data[i] = data[i].replace("\n"," ")
if select=="辞書１":
    dict_1={data[0]:data[1],data[2]:data[3],data[4]:data[5]}
    print("これは辞書１です。　",dict_1)
else:
    dict_2={data[0]:data[1],data[2]:data[3],data[4]:data[5]}
    print("これは辞書２です。 ",dict_2)
