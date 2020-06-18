# -*- coding: utf-8 -*-

from janome.tokenizer import Tokenizer
import numpy as np
import matplotlib.pyplot as plt
import pickle


##########################
# モデルを読み込み、指定した偉人について
# 教師データ生成
##########################

def load_model(file_name):
    """指定したファイルを読み込む関数"""
    with open(file_name + ".binaryfile", "rb") as f:
        model = pickle.load(f)
    return model


def get_word_tfidf_list(tfidf_array, feature_names, ijin_id=0):
    """単語:とtfidf値のリストを返す関数
        引数で指定した偉人について、(単語: tfidf値)を要素とするリストを、
        tdifd値の降順にソートして返す。
        単語は、全偉人分。

    Args: 
    tfidf_array:
    全偉人分のtf_idf値のarray

    feature_names:
    全偉人分の単語のarray

    Returns: 
    word_tfidf_list:list
    （単語: tfidf値）のタプルを要素とするリスト
    """
    vec = tfidf_array[ijin_id]
    index = np.argsort(vec)
    words = feature_names[index]
    tfidf = vec[index]

    word_tfidf_list = []
    for i in range(len(vec)):
        word_tfidf_list.append(tuple([words[-i], tfidf[-i]]))

        # 開発用：###########################################
        # # (単語: tidf値)のリストをターミナルに出力
        # print(f"{words[-i]} : {tfidf[-i]}\n", end="")

    return word_tfidf_list


def receive_input(ijin_id=0):
    """引数で指定した偉人について、入力を受け付ける関数"""

    input_text = input(f"{ijin_id}について知っていることを入力してください")
    return input_text


def get_input_keitaiso_set(input_text):
    """入力文章を形態素分解して、ユニークな形態素の
    要素を格納したリストを返す関数"""

    tokenizer = Tokenizer()
    input_keitaiso_list = tokenizer.tokenize(input_text, wakati=True)

    # 要素をユニークにする
    # 同じ単語を連続で入力してもスコアに加算されるのは1回のみとするため
    input_keitaiso_set = set(input_keitaiso_list)

    return input_keitaiso_set

##########################
# 教師データと
# 受付た入力のユニークな形態素を要素リスト
# を受け取り、スコア算出を行うクラス
##########################

# calc_score_1で使用


class Scoring(object):

    def __init__(self, ijin_id, ijin_name, word_tfidf_list):
        # インスタンス変数を定義
        self.ijin_id = ijin_id
        self.ijin_name = ijin_name
        self.word_tfidf_list = word_tfidf_list
        # self.input_keitaiso_set = input_keitaiso_set

        self.tfidf_max = 0.0

    def get_top_words_list(self, num=30):
        """tf_idf値の降順でn個の単語を取得してリスト化する関数
        TODO top30もしくは40にしてもよいか"""

        top_words_list = []
        for i in range(num):
            top_words_list.append(self.word_tfidf_list[i][0])

        return top_words_list

    def calc_tfidf_max(self):
        """calc_score_2で使用。
        該当の偉人にかかる全単語のtfidf値の累計
        TODO 極端にtfidf値が高い単語の値は除く"""

        for tuple_ in self.word_tfidf_list:

            # 本人の名前など、tfidf値が高すぎるためtfidf値の合計値には含めない
            if tuple_[0] in self.ijin_name:
                continue

            # 単語のtfidf値を足していく
            else:
                self.tfidf_max += tuple_[1]

        return self.tfidf_max

    def sigmoid(self, x):
        """スコア2の計算用。入力をシグモイド関数にかける
        TODO sigmoid()もしくはtanhのいずれかを採用する"""

        return 1.0 / (1.0 + np.exp(-x))

    def tanh(self, x):
        """calc_score_2で使用。入力をtanh関数にかける
        TODO sigmoid()もしくはtanhのいずれかを採用する"""

        return np.tanh(x)

    def calc_score_1(self, input_keitaiso_set, top_words_list):
        """70点分のスコアを算出する関数
        該当の偉人のtfidfリストの上位n位以内の単語が含まれていたらx点ずつ、
        最大nx点を付与する"""
        count = 0
        for keitaiso in input_keitaiso_set:
            if count == 5:
                break

            # 本人の名前など、tfidf値が高すぎるためtfidf値の合計値には含めない
            # self.ijin_name: 「板垣退助」などの本名フルネームのテキストデータ
            elif keitaiso in self.ijin_name:
                continue

            if keitaiso in top_words_list:
                count += 1

        score_1 = 5 * count  # ハイパーパラメータ1(スコア1:スコア2の割合)

        return score_1

    ##########################
    # score_2の算出
    ##########################

    def calc_score_2(self, input_keitaiso_set, hyper_param=7):  # ハイパーパラメータ2(tanh(x)の横軸の拡大幅)
        """30点分のスコアを算出する関数
        教師データに含まれる単語が存在したときに、そのtfidf値を加算していき、スコアに換算する関数"""

        tfidf = 0.0
        for keitaiso in input_keitaiso_set:
            for tuple_ in self.word_tfidf_list:

                # TODO 本人の名前など、tfidf値が高すぎるためtfidf値の合計値には含めない
                if tuple_[0] in self.ijin_name:
                    continue

                # 形態素が教師データにあったらその単語のtfidf値を加算
                elif keitaiso == tuple_[0]:  # inではなく==
                    tfidf += tuple_[1]

        # tfidf累積を0からhyper_paramの間に拡大した上で、シグモイド関数にかける
        # yの値は0~0.5 --x60--> 0~30の範囲
        x = tfidf * hyper_param / self.tfidf_max

        # TODO シグモイドとtanhのどちらの数式にするか決める
        # score_2 = (sigmoid(y) -0.5) * 60
        score_2 = self.tanh(x) * 75  # ハイパーパラメータ1(スコア1:スコア2の割合)

        return score_2

    def draw_calc_score_2(self, hyper_param=7):
        """(検証用) 
        入力文章に、教師データに含まれる単語のうちtfidf値が高いものから順に、
        1つずつ単語が増えた場合に、どのようにスコアが上昇するかをmatplotlibで描画する関数"""

        # 当該偉人の文章群に含まれる単語の総数
        count = 0
        for tuple_ in self.word_tfidf_list:
            if tuple_[1] > 0.0:
                count += 1

        # print("count:", count) # 開発用

        # x座標(=tfidf累積)、y座標(=スコア)を格納
        X = []
        Y_tanh = []
        Y_sigmoid = []

        # 含める単語の数を1ずつ増やしながら、tfidf値とスコアの関係を調べる
        for i in range(count):
            x = 0.0

            for tuple_ in self.word_tfidf_list[:i+1]:
                # 本人の名前はtfidf値が高すぎるため除く
                # self.ijin_name: 「板垣退助」などの本名フルネームのテキストデータ
                if tuple_[0] in self.ijin_name:
                    continue

                else:
                    x += tuple_[1]
                    self.tfidf_max += tuple_[1]  # 外側for文の最後の1回の処理のみ反映される
            X.append(round(x, 4))

        # Xの値を0から5の範囲に拡大 # TODO 5はハイパーパラメータ
        X = np.dot(X, hyper_param / self.tfidf_max)

        # xの値をシグモイド関数にかけてy軸を0.5減らす
        # 及びtanh関数にかけて出力された値yに、30かけてYに格納
        for x in X:
            y = self.sigmoid(x) - 0.5
            Y_sigmoid.append(y * 60)

            y = self.tanh(x)
            Y_tanh.append(y * 30)

        # numpy array型に変換（出力が見やすいため）
        Y_sigmoid = np.array(Y_sigmoid)
        Y_tanh = np.array(Y_tanh)

        # 検証用に出力するため
        for i in range(len(X)):
            print(f"({X[i]}. {Y_sigmoid[i]})")
        for i in range(len(X)):
            print(f"({X[i]}. {Y_tanh[i]})")

        # 開発用：出力用
        # print("X:", X)
        # print("Y_sigmoid", Y_sigmoid)
        # print("tfidf_max", self.tfidf_max)

        # シグモイドとtanh両方の関数を同時に描画して1つの画像に保存
        plt.plot(X, Y_sigmoid)
        plt.plot(X, Y_tanh)
        plt.xlabel("total_of_tfidf")
        plt.ylabel("score")
        plt.savefig("./result/tfidf_score_draw.jpeg")

    def calc_total_score(self, score_1, score_2):
        """スコア1と2を足し合わせる"""
        total_score = score_1 + score_2
        total_score = round(total_score, 1)
        return total_score


def main(ijin_name, input_text):
    # ijin_name=フルネームのstr型でwebからくる
    ijin_dict = {"fujiwara": (0, "藤原道長"), "minamoto": (1, "源頼朝"), "oda": (2, "織田信長"), "saigo": (3, "西郷隆盛"),
                 "tenji": (4, "天智天皇"), "taira": (5, "平清盛"), "tokugawa": (6, "徳川家康"), "toyotomi": (7, "豊臣秀吉"),
                 "sakamoto": (8, "坂本龍馬"), "date": (9, "伊達政宗"), "natume": (10, "夏目漱石"), "noguchi": (11, "野口英世"),
                 "rikyu": (12, "千利休"), "ito": (13, "伊藤博文"), "katsu": (14, "勝海舟"), "shotoku": (15, "聖徳太子"),
                 "ashikaga": (16, "足利義満"), "itagaki": (17, "板垣退助"), "iwakura": (18, "岩倉具視"), "inou": (19, "伊能忠敬"),
                 "narusawa": (20, "narusawa")}

    for ijin in ijin_dict.values():
        if ijin[1] == ijin_name:
            ijin_id = ijin[0]

        # 教師データの準備
    tfidf_array = load_model(
        "./ijin_game_api/views_functions/syntactic_analysis/saved_model/tfidf_array")
    feature_names = load_model(
        "./ijin_game_api/views_functions/syntactic_analysis/saved_model/feature_names")
    word_tfidf_list = get_word_tfidf_list(
        tfidf_array, feature_names, ijin_id=ijin_id)

    # 偉人について入力受付、形態素セット生成
    input_keitaiso_set = get_input_keitaiso_set(input_text)

    # スコアリングするクラスのインスタンス化
    calc_score = Scoring(ijin_id=ijin_id, ijin_name=ijin_name,
                         word_tfidf_list=word_tfidf_list)

    # 検証用###############################################
    # ファイルに単語:ifidf値のリストを出力
    # get_result_file(tfidf_array, feature_names)
    # tfidf累積とスコアの関係を出力して描画する
    # draw_calc_score_2(word_tfidf_list)

    # スコア算出の準備
    top_words_list = calc_score.get_top_words_list(num=30)
    calc_score.calc_tfidf_max()

    # スコアの算出
    score_1 = calc_score.calc_score_1(input_keitaiso_set, top_words_list)
    score_2 = calc_score.calc_score_2(input_keitaiso_set, hyper_param=10)

    # 合計スコア表示
    total_score = calc_score.calc_total_score(score_1, score_2)
    print(f"------------------スコアの内訳------------------")
    print(f"スコア1：{score_1} 点\nスコア2:{score_2} 点")

    # 開発用
    print(f"-----------{ijin_name}の重要単語上位30位-----------")
    print(f"-----------※本人の名前は除く※-----------")
    for i, tuple_ in enumerate(word_tfidf_list):
        if tuple_[0] in calc_score.ijin_name:
            continue
        else:
            print(tuple_)
            i += 1
            if i == 30:
                break

    return int(round(total_score, 0))


# 開発用：単語: tfidf値を検証するため
if __name__ == "__main__":
    tfidf_array = load_model(
        "./saved_model/tfidf_array")
    feature_names = load_model(
        "./saved_model/feature_names")
    word_tfidf_list = get_word_tfidf_list(
        tfidf_array, feature_names, ijin_id=17)
    for i, tuple_ in enumerate(word_tfidf_list):

        print(tuple_)
        i += 1
        if i == 100:
            break
