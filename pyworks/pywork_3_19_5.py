"""
問題@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
上記のおみくじを、吉が最も出やすく、大吉と凶は最も出にくく、中吉と小吉はその中間にしてください。
問題@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""
import random

#fortuneにくじの中身をいれる
fortune = ["大吉","中吉","吉","小吉","凶"]

#random.choicesでリストからweightにしたがって、要素を一つ抽出する。さらにdoreに格納する
dore = random.choices(fortune,[1,5,10,5,1])
print("あなたの今年は！",dore,"です！")


