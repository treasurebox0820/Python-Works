"""
問題@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
randomモジュールを使っておみくじを作ってください。
（ヒントは下記）•random.choice(): 引数にリストを与えると要素をランダムに取り出す。
•おみくじの要素は、大吉、中吉、吉、小吉、凶、の５種類。
問題@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


"""
import random

fortune = ["大吉","中吉","吉","小吉","凶"]

dore = random.choice(fortune)

print("あなたの今年は！",dore,"です！")