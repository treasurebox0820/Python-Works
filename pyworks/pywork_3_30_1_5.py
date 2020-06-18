class Question2:
    """
    """
    def __init__(self):
        """
        """
        #問題の解答とヒントをインスタンス属性に持ち
        self.quest ="質問"
        self.hint = "ヒント"
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
        """
        回答を取得する関数
        """
        return self.answer
if __name__=="__main__":
    a = Question()
    print(a.get_answer())