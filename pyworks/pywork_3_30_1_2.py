from pywork_3_30_1 import Question
import random
class Calculation(Question):
    def get_number(self):
        super().get_question()
        """
        計算の数を取得する
        """
        self.given1 = random.randrange(10,100)
        self.given2 = random.randrange(10,100)
        #検証、selfで返したらgiven1とgiven2は出てくるか
        return self
    def get_question(self):
        """
        """
        #問題文のインスタンスに格納
        self.quest = ("{}×{}を計算してください。".format(self.given1,self.given2))
        print(self.quest)
    def get_hint(self):
        """
        """
        self.hint = "ひっ算をするときは、位を意識しましょう。"
        print(self.hint)
    def get_answer(self):
        """
        """
        self.answer = f"答えは:{self.given1 * self.given2}"
        #"答えは:{}".format(self.given1*self.given2)
        print(self.answer)

if __name__ == "__main__" : 
    i=0   
    while i<5:
        z1 = Calculation()
        print(z1.get_number())
        z1.get_question()
        z1.get_hint()
        z1.get_answer()
        i +=1
