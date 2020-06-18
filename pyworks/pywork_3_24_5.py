"""
1.「辞書(dict) と 繰り返し処理 & ファイル入出力」のワークAの続きです。
下記の要件を満たすようにプログラムを更新してください。
•ファイルの保存先をカレントディレクトリの下の dicfiles というディレクトリにしてください。クリア
•dicfiles というディレクトリがなければ新規作成してください。クリア
•保存するファイルが存在しない場合は新規作成し、ある場合は、新しいデータのみを追加してください。
必要なスキル＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠
os
・ファイルを作る
・ディレクトリかどうか調べる
    os.path.isfile(///////)
・ディレクトリの存在を確認する
    os.path.exists("dicfiles")
pathlib
"""
import os
import pathlib

if not os.path.exists("dicfiles"):
    os.mkdir("dicfiles")
    os.chdir("dicfiles")
else:
     os.chdir("dicfiles")

mario_dic={'Mario': 'マリオ', 'Luigi': 'ルイージ', 'Wario': 'ワリオ', 'waLuigi': 'ワルイージ', 'Yoshi': 'ヨッシー'}
mario_dic2={'Peach': 'ピーチ', 'DK': 'ドンキーコング', 'Bowser': 'クッパ', 'Boo': 'テレサ'}

if not os.path.exists("mario.txt"):
    #マリオ辞書の内容をsampleテキストに書き込む
    with open("mario.txt","w") as f:
        for key, value in mario_dic.items():
            f.write(key+":"+value+"\n")

    #sampleの内容を読み込む
    luigi_dic={}
    with open("mario.txt","r") as f:
        for line in f:
            #
            luigi_dic[line.strip().split(":")[0]] = (line.strip().split(":")[1])

    print(luigi_dic)
else:
    with open("mario.txt","a") as f:
        for key, value in mario_dic2.items():
            f.write(key+":"+value+"\n")

    #sampleの内容を読み込む
    luigi_dic={}
    with open("mario.txt","r") as f:
        for line in f:
            #
            luigi_dic[line.strip().split(":")[0]] = (line.strip().split(":")[1])

    print(luigi_dic)
    