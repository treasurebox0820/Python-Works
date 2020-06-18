"""
2.次のようなプログラムを作成してください。
　1.辞書データをプログラム内で定義して、そのデータをファイルに書き出します。
　2.１で書き出したファイルに書かれたデータをプログラムで読み込んで、
辞書に読み込み、それを表示します。
 ヒント：１の課題を行う際は、２でファイルからデータを読み込むことを前提にして読み込みしやすい形式で
 ファイルに書き出しておくと良い。
 手順
 1.辞書型のデータをつくる
 2.
 
 """
mario_dic={'Mario': 'マリオ', 'Luigi': 'ルイージ', 'Wario': 'ワリオ', 'waLuigi': 'ワルイージ', 'Yoshi': 'ヨッシー'}

#マリオ辞書の内容をsampleテキストに書き込む
with open("sample.txt","w") as f:
    for key, value in mario_dic.items():
        f.write(key+":"+value+"\n")

#sampleの内容を読み込む
luigi_dic={}
with open("sample.txt","r") as f:
    for line in f:
        line.strip().split(":")[0]
        luigi_dic[line.strip().split(":")[0]] = (line.strip().split(":")[1])

print(luigi_dic)


