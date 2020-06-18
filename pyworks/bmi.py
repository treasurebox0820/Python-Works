"""
1.体型を判定するために使われる BMI (Body Mass Index) を計算して判定するプログラムを作ってください。
BMIの計算式は下記です。
BMI = 体重(kg) / (身長(m)) ** 2
　1.身長(cm)と体重(kg)の値の入力を受け付けます。OK
　2.BMI の計算を行い計算結果を出力します。
　3.判定基準１に従って判定結果を出力します。
　4.BMIの計算を行う関数 calc_bmi は身長と体重を受け取りBMI値を返す。
　5.判定を行う関数 judge_bmi は BMI値を受け取り結果を文字列で返す。
　6.プログラムは bmi.py という名前のモジュールとして保存してください。
6はすでにOK。

修正ポイント\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
少数の表示を短くする。
0の割り算への対応をかんがえる
西谷発表\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
for文と辞書をつかって
"""
#4.BMIの計算を行う関数 calc_bmi は身長と体重を受け取りBMI値を返す。
def cal_bmi(height,weight):
    """
    BMIの計算を行う関数 calc_bmi は身長と体重を受け取りBMI値を返す。
    """
    BMI_value=int(weight)/(float(height/100))**2
    return BMI_value
#5.判定を行う関数 judge_bmi は BMI値を受け取り結果を文字列で返す。
def judge_bmi(judge_num):
    if judge_num < 18.5:
        judge_restult="やせ型"
    elif judge_num < 25:
        judge_result="標準"
    elif judge_num < 30:
        judge_restult = "肥満"
    else:
        judge_restult = "高度な肥満"
    return judge_restult

if __name__== "__main__":
    #身長、体重を入力
    #　1.身長(cm)と体重(kg)の値の入力を受け付けます。OK
    height = input("身長を入力してください。")
    weight = input("体重を入力してください。")

    your_BMI = cal_bmi(height,weight)
    #2.BMI の計算を行い計算結果を出力します。OK
    print("あなたのBMIは{}".format(your_BMI))
    #3.判定基準１に従って判定結果を出力します。
    print("あなたの体系は{}".format(judge_bmi(your_BMI)))
    

