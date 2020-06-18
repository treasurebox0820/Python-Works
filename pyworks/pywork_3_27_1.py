class Sample:
   """先頭アンダースコアによる隠蔽の確認"""
   __test=1
   _test=1
   __test_=1
   __test__ =1
   def __init__(self):
       self.a = 1
       self._b = 1
       self.__c = 1
       self.__d_ = 1
       self.__e__ = 1
if __name__ == "__main__":
    s = Sample()
    #print(s.a, s._b, s.__e__)
    #print(s.__c)    # AttributeErrorになる
    #print(s.__d_)   # AttributeErrorになる

    #クラス変数についても同じこと
    #print(s.__test)   # AttributeErrorになる
    #print(s._test) 
    #print(s.__test_)   
    print(s.__test__)   # AttributeErrorになる