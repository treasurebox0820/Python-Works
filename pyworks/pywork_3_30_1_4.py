"""
4.さらに、間違い探し問題、虫食い問題を作るプログラムを作成してください。
"""
from pywork_3_30_1_5 import Question2
import random

class Finding_error(Question2):
    def make_question(self):
        dict_error = {"走":"従","轟":"晶","乃":"ん","腐":"店"}
        key_error = random.choice(["走","轟","乃","腐"])
        kazu = random.randrange(1,20)
        str_error = key_error * (kazu) + dict_error[key_error]+key_error *(20-kazu)
        self.quest = f"{str_error}の中に一つだけ仲間はずれがいるよ。何番目の漢字かな？"
        self.hint = "本当に全部同じ漢字かな？本当に？"
        self.answer =f"{kazu+1}番目が違う漢字だよ。"
        return self

if __name__ == "__main__":
    test = Finding_error()
    test.make_question()
    print(f"{test.quest}\n{test.hint}\n{test.answer}")
    print(test.*) 