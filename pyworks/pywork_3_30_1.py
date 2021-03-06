"""
1.小学生向けの算数と国語の問題を生成するプログラムを作る。
　1.問題の解答とヒントをインスタンス属性に持ち、
次のようなメソッドをもつ「問題のクラス」を作成してください。
ただし、メソッドの中身は実装せず print() でメソッドが呼ばれたことを表示のみします。
　　1.問題を作成する
　　2.問題文を取得する
　　3.答え文を取得する
　　4.ヒント文を取得する
　2.問題のクラスを継承して、計算問題を実装してください。
計算問題５問とそのヒントと答えを出力するプログラムを作成してください。
　3.これまでに作成済みのいずれかのクラスを継承してたぬき問題を実装してください。
 （ここまで１時間）
　4.さらに、間違い探し問題、虫食い問題を作るプログラムを作成してください。
　5.上記、４種類の問題から５つの問題をランダムに生成するプログラムを作成してください
"""
class Question:
    """
    """
    def __init__(self):
        """
        """
        #問題の解答とヒントをインスタンス属性に持ち
        self.quest = "質問"
        self.hint = "ヒント"
        self.given1 = "No Value"
        self.given2 = "No Value"
        self.answer = "答え"

    def make_question(self):

        """
        問題を作る関数。
        すべての問題を作る作業において共通することは、この関数から
        問題のタイプを識別する＆問題の値を取得する
        """

    def get_question(self):
        """
        問題を取得する関数。
        """

        return self.quest
    def get_hint(self):
        """
        ヒントを取得する関数、
        """
        return self.hint
    def get_answer(self):
        return
        """
        回答を取得する関数
        """
if __name__=="__main__":
    a = Question()
    print(a.hint)
    print(a.quest)