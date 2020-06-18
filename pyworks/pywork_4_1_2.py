"""
【ワーク 6-2：反復子とジェネレータ　2/2】
1. ユーザーID、身長、体重、肥満度の分類、の４つの項目からなる CSV データ
（カンマ区切りのテキスト）を乱数を使って１万人分（１万行）作成し、
それをファイル bmi_data.csv に保存してください。
　1. 乱数を使うときは、乱数の種を 42 に固定してください。
　2. 身長、体重の上限と下限は現実的な範囲を自分で決めてください。
　3. 肥満度の分類は、BMIの値に応じて下記の判定基準に従って割り当ててください。
{痩せ型:18.5未満、標準:25.0未満、肥満:30.0未満、高度な肥満:30.0以上}
2. 上記のファイルの先頭５行のみを表示するプログラムを実行に時間がかからない方法で作成してください。
3. 上記ファイルの先頭20行のデータを読み込んで、ユーザーID順、身長順、体重の順に並び替えて表示してください。
4. 上記ファイルの１万件全てのデータから身長と体重の最小値、最大値、平均値を計算して表示してください。
5. （時間が余ったら）上記ファイルの１万件全てのデータから肥満度の分類の頻度（出現度数 または 度数分布ともいう）とそれらの割合を表示してください。

"""
import random
class BMI():
    """
    """
    classname = "一組"

    def __init__(self):
        self.id = id
        self.weight = "No Value"
        self.height = "No Value"
        self.bmi = "No Value"
        self.body_is = "No Value"
    def cal_bmi(self,height,weight):
        """
        BMIの計算を行う関数 calc_bmi は身長と体重を受け取りBMI値を返す。
        """
        BMI_value=int(weight)/(float(height/100))**2
        return BMI_value
#5.判定を行う関数 judge_bmi は BMI値を受け取り結果を文字列で返す。
    def judge_bmi(self,judge_num):
        if judge_num < 18.5:
            judge_result="やせ型"
        elif judge_num < 25:
            judge_result="標準"
        elif judge_num < 30:
            judge_result = "肥満"
        else:
            judge_result = "高度な肥満"
        return  judge_result
if __name__ == "__main__":
    random.seed(42)
    with open("sample3.txt","w") as f:
        for i in range(1,10001):
            you = BMI()
            you.weight = random.randrange(20,101)
            you.height = random.randrange(100,230)
            you.bmi = you.cal_bmi(you.height,you.weight)
            you.id = i
            you.body_is = you.judge_bmi(you.bmi)
            f.write(f"{you.id}, {you.weight}kg, {you.height}cm, {you.body_is}\n")