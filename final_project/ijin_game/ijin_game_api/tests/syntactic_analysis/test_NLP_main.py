import unittest

from NLP_main2 import load_model
from NLP_main2 import get_word_tfidf_list
from NLP_main2 import receive_input
from NLP_main2 import get_input_keitaiso_set

import NLP_main2


class LoadModelTest(unittest.TestCase):
    pass


class TestReceiveInputTest(unittest.TestCase):
    def test_receive_input(self):
        # コンソールには「テスト」と入力する
        self.assertEqual("テスト", receive_input())


class GetInputKeitaisoSetTest(unittest.TestCase):
    def test_get_input_keitaiso_set(self):
        # ########### 準備と検証1 ###############
        # 普通の文章
        text = "道長は彰子を後一条天皇に嫁がせた。"
        set_ = {"道長", "は", "彰子", "を", "後一条天皇", "に", "嫁が", "せ", "た", "。"}
        self.assertSetEqual(set_, get_input_keitaiso_set(text))

        # ########### 準備と検証2 ###############
        # 同じ単語が2回登場する
        text = "道長の娘は彰子。彰子は後一条天皇の妻"
        set_ = {"道長", "の", "娘", "。", "は", "彰子", "は", "後一条天皇", "妻"}
        self.assertSetEqual(set_, get_input_keitaiso_set(text))

        

class ScoringTest(unittest.TestCase):

    def setUp(self):
        ijin_name = 0 # 偉人名
        word_tfidf_list = [
        ("道長", 0.8784298842949801), # tfidf値の計算には含めない
        ("彰子", 0.15301681855460944),
        ("御堂", 0.15301681855460944),
        ("法成寺", 0.12468037067412621),
        ("摂関", 0.11901308109802958),
        ("一条天皇", 0.10767850194583628),
        ("道隆", 0.1051636715542712),
        ("中宮", 0.09067663321754633),
        ("三条", 0.07772967027924393),
        ("頼通", 0.0736747644892564),
        ("出家", 0.07315733673340605),
        ("寛仁", 0.06800747491315975),
        ("後一条天皇", 0.06800747491315975),
        ("妍子", 0.06800747491315975),
        ("この世", 0.062340185337063106),
        ("966", 0.056672895760966464),
        ("中期", 0.05486800255005454),
        ("望月", 0.051005606184869816),
        ("みち", 0.04572333545837878),
        ("外戚", 0.041151001912540904),
        ("土御門", 0.041151001912540904), #21位なのでtop_20からは除外
        ]

        self.scoring = NLP_main2.Scoring(
            ijin_name=ijin_name,
            word_tfidf_list=word_tfidf_list,
        )

    def test_get_top_words_list(self):
        # ########### 準備 ###############
        list_ = [
            "道長","彰子", "御堂", "法成寺", "摂関",
            "一条天皇", "道隆", "中宮", "三条", "頼通",
            "出家", "寛仁", "後一条天皇", "妍子", "この世",
            "966", "中期", "望月", "みち", "外戚"
        ]
        # 引数で20を指定するとき
        # ########### 検証 ###############
        self.assertEqual(list_, self.scoring.get_top_words_list(20))


    def test_calc_tfidf_max(self):
        # ########### 準備 ###############
        tfidf_max = (
        0.15301681855460944
        + 0.15301681855460944
        + 0.12468037067412621
        + 0.11901308109802958
        + 0.10767850194583628
        + 0.1051636715542712
        + 0.09067663321754633
        + 0.07772967027924393
        + 0.0736747644892564
        + 0.07315733673340605
        + 0.06800747491315975
        + 0.06800747491315975
        + 0.06800747491315975
        + 0.062340185337063106
        + 0.056672895760966464
        + 0.05486800255005454
        + 0.051005606184869816
        + 0.04572333545837878
        + 0.041151001912540904
        + 0.041151001912540904
        )# 1.6347421209568291
        # ########### 検証 ###############
        self.assertAlmostEqual(tfidf_max, self.scoring.calc_tfidf_max())


    def test_sigmoid(self):
        self.assertAlmostEqual(0.7310585786, self.scoring.sigmoid(1))
        self.assertAlmostEqual(0.8807970779, self.scoring.sigmoid(2))
        # 計算に使ったウェブサイト：https://keisan.casio.jp/exec/system/1541125775
    

    def test_tanh(self):
        self.assertAlmostEqual(0.7615941559, self.scoring.tanh(1))
        self.assertAlmostEqual(0.9640275800, self.scoring.tanh(2))
       # 計算に使ったウェブサイト：https://keisan.casio.jp/exec/system/1541125775


    def test_calc_score_1(self):
        # ########### 準備 ###############
        top_words_list = [
            "道長","彰子", "御堂", "法成寺", "摂関",
            "一条天皇", "道隆", "中宮", "三条", "頼通",
            "出家", "寛仁", "後一条天皇", "妍子", "この世",
            "966", "中期", "望月", "みち", "外戚"
        ]

        # ########### 検証1 ###############
        # 「道長」を除き2単語を含む場合
        input_keitaiso_set = {
            "道長", "は", "彰子", "を", "後一条天皇", "に", "嫁が", "せ", "た"
        }
        score = 14 * 2
        self.assertEqual(score, self.scoring.calc_score_1(input_keitaiso_set, top_words_list))

        # ########### 検証2 ###############
        # 5単語以上含む場合は上限は70点になる
        input_keitaiso_set = {
            "道長", 
            "彰子", "頼通", "後一条天皇", "摂関", "中宮", "道隆", "法成寺"
        } # 該当単語は7つ　※「道長」除く
        score = 70
        self.assertEqual(score, self.scoring.calc_score_1(input_keitaiso_set, top_words_list))



    def test_calc_score_2(self):

        # ########### 準備 ###############
        input_keitaiso_set = {
            "道長", 
            "彰子", "頼通", "後一条天皇",  "摂関", "中宮", "道隆", "法成寺"
        }
        tfidf = (
            0.15301681855460944 # 彰子
            + 0.0736747644892564 # 頼通
            + 0.06800747491315975 # 後一条天皇
            + 0.11901308109802958 # 摂関
            + 0.09067663321754633 # 中宮
            + 0.1051636715542712 # 道隆
            + 0.12468037067412621 # 法成寺
        ) # 0.7342328145009989
        
        tfidf_max = 1.6347421209568291
        y = 3.144000289476068 # tfidf * 7 / self.tfidf_max
        tanh_y = 0.99628995081735
        score = 29.8886985245205 # tanh(y) * 30
        
        # 検証対象の関数で使用するtfidf_max属性を生成
        self.scoring.tfidf_max = 1.6347421209568291

        # ########### 検証 ###############
        self.assertAlmostEqual(score, self.scoring.calc_score_2(input_keitaiso_set, hyper_param=7))

    
    def test_calc_total_score(self):
        self.assertEqual(81, self.scoring.calc_total_score(56, 24.9999))
        self.assertEqual(39, self.scoring.calc_total_score(14, 25.0001))
