"""
　2.random モジュールを使って、任意の名前と成績を 100 人分生成してファイルに保存してください。
"""
import random
class Grade():
    """
    """
    classname = "一組"

    def __init__(self,name,japanese ,english, math):
        self.name = name
        self.japanese = japanese
        self.english = english
        self.math = math
if __name__ == "__main__":
    with open("sample3.txt","w") as f:
        f.write("名前  国語  英語  数学\n")
        for i in range(1,101):
            i = Grade("A"+str(i),random.randrange(1,101),random.randrange(1,101),random.randrange(1,101))
            f.write("{}    {}    {}    {}\n".format(i.name,i.japanese, i.english,i.math))