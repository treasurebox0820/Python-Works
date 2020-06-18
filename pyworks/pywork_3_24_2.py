"""
2.次のようなプログラムを作成してください。
　1.辞書データをプログラム内で定義して、そのデータをファイルに書き出します。
　2.１で書き出したファイルに書かれたデータをプログラムで読み込んで、
辞書に読み込み、それを表示します。
 ヒント：１の課題を行う際は、２でファイルからデータを読み込むことを前提にして読み込みしやすい形式で
 ファイルに書き出しておくと良い。

制作手順||||||||||||||||||||||||||||||||||||||
1.

マッピングって何？

fがiterableってのに気が付かなかった！


"""

word="犬\nいぬ\n猫\nねこ\n狐\nきつね\n"
with open("sample.txt","a",encoding="utf_8_sig") as f:
	f.write(word)
with open("sample.txt","r",encoding="utf_8_sig") as f:  
    data=f.readlines()
    for i in range(len(data)):
        data[i] = data[i].replace("\n"," ")

dict_={data[0]:data[1],data[2]:data[3],data[4]:data[5]}
print(dict_)


"""
    for i in range(len(data)):
        data[i] = data[i].replace("\n"," ")
"""





