"""
　3.これまでに作成済みのいずれかのクラスを継承してたぬき問題を実装してください。
 （ここまで１時間）
"""
import random
from pywork_3_30_1_2 import Calculation

class Ta(Calculation):
    def make_question(self):
        """
        ５つの言葉のリスト,ta_words_listから１つの言葉を選ぶ関数
        """
        super().get_question()
        #５つのワードリストから１つをとる
        ta_words_list= ["はながっぱ","いりこだし","らららんど","しものせき","ことおうしゅう"]
        self.given1 = ta_words_list[random.randrange(1,5)]

        #選んだ言葉を分解し、を一度リストにして、10回「た」を加える
        i=0
        new_list = list(self.given1)
        while i < 10:
            random_index = random.randrange(1,len(new_list))
            #insertで
            new_list.insert(random_index,"た")
            i += 1      
        #last_strは最後にたが入った文字を格納する文字列
        last_str = ""
        for x in new_list:
            last_str += x
        
        #self.questに問題を格納
        self.quest =f"{format(last_str)}、から「た」をぬいて、隠れた文字を答えよ"     
        
        #self.hintにヒントを格納
        self.hint = "「た」を全部抜いた時に出てくる言葉を冷静に探すんだよ！"
        self.answer = f"答えは:{self.given1}"
        return self
    def get_question(self):
        """
        """
    def get_hint(self):
        """
        """
        print(self.hint)
    def get_answer(self):
        """
        """

        print(self.answer)



if __name__ == "__main__":
    #インスタンス生成
    ta = Ta()
    ta.make_question()
    print(f"{ta.quest}\n{ta.hint}\n{ta.answer}")