"""
2.１で作成したモジュールを利用(import)して、下記の要件を満たす別のプログラム（モジュール）を作成してください。
　1.プログラムを起動したらユーザーからの入力を待ち続け、何度も計算できるようにします。
　2.身長または体重の入力のときに quit と入力されたらプログラムを終了します。
　3.入力文字列が数字でないか、数字でも値が常識的な範囲から外れる場合は再度入力を受け付けます。
　4.判定基準２に従った判定結果を出力します。
　5.プログラムファイルは bmi_2011.py としてください。

5はモジュールの名前がbmi_2011.pyなのでOK
課題\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
時間は間に合わなかったがnew_judge_bmiがjudge_bmiを踏襲できる形がよかった。

"""
from bmi import cal_bmi
from bmi import judge_bmi



#　4.判定基準２に従った判定結果を出力します。クリア
def new_judge_bmi(judge_num):
    if judge_num < 18.5:
        judge_result="やせ型"
    elif 18.5 <= judge_num < 25:
        judge_result="標準"
    elif 25 <= judge_num < 30:
        judge_result="肥満(一度)"
    elif 30 <= judge_num < 35:
        judge_result="肥満(二度)"
    elif 35 <= judge_num < 40:
        judge_result="肥満(三度)"
    else:
        judge_result="肥満(四度)"
    return judge_result

print("BMIの計算と、体形を判断するプログラムを実行します。")
#1.プログラムを起動したらユーザーからの入力を待ち続け、何度も計算できるようにします。OK

#入力文字列が数字でないか、数字でも値が常識的な範囲から外れる場合は再度入力を受け付けます。OK
while True:
    weight = input("体重(kg)を入力してください。")
    height = input("身長(m)を入力してください。")
    if weight == "quit" or height == "quit":
        break 
    if not  (1 < float(height) < 3 and 10 < float(weight) < 300):
        print("適切な範囲での入力をお願いします。")
        continue 
    else:
        print("あなたのBMIは{}です。体形は{}です。".format(round(cal_bmi(height,weight)),new_judge_bmi(cal_bmi(height,weight))))
print("プログラムを終了します。")

"""
def new_judge_bmi(judge_num):
    if judge_num < 18.5:
        judge_result="やせ型"
    elif 18.5 <= judge_num < 25:
        judge_result="標準"
    elif 25 <= judge_num < 30:
        judge_result="肥満(一度)"
    elif 30 <= judge_num < 35:
        judge_result="肥満(二度)"
    elif 35 <= judge_num < 40:
        judge_result="肥満(三度)"
    else:
        judge_result="肥満(四度)"
    return judge_result
"""