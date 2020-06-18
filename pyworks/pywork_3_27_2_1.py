class Grade():
    """
    
    """
    classname = "一組"

    def __init__(self,name,japanese ,english, math):
        """
        初期化メソッド
        arguments: name,japanese, english, math
        """
        self.name = name
        self.japanese = japanese
        self.english = english
        self.math = math
    
    def show_attribute(self)
        """
        
        """
        print(self.name, self.japanese, self.english, self.math)

if __name__ == "__main__":
#インスタンスを５人分生成
taro = Grade("太郎",32,34,39)
ito = Grade("伊藤",98 ,12, 74)
kon = Grade("懇",58 ,72, 34)
zen = Grade("善",68 ,12, 34)
yama = Grade("山",43, 80, 39)


show_attribute(taro)
print(type(taro))
print(taro.name)
