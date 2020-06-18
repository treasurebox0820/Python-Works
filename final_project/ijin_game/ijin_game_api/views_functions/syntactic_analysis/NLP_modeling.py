# -*- coding: utf-8 -*-
import numpy as np
import glob
import pickle

from janome.analyzer import Analyzer
from janome.tokenizer import Tokenizer
from janome.tokenfilter import POSKeepFilter, CompoundNounFilter

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer


#############################
# 特定のタイトル名の複数のファイルから
# テキストデータを取得する
#############################
"""globの使い方
glob.glob("./text_file/scraping_1/0*.txt")
->ディレクトリにおける、0から始まるファイル名のものをすべて取得する"""


def get_sentence_list(num):
    """各偉人につき、格納したファイルから該当のテキストファイルを読み込みリストに格納して返す関数

    Args:
    num: int, 読み込む偉人の数

    Returns:
    sentence_list: list, 
    偉人1人につき、該当するテキストファイル全てから読み込んだ文字列の集合を1要素とする
    """
    # 偉人1人につき1つの文章群を要素として格納するリスト
    sentence_list = []

    for i in range(num):
        paths = glob.glob(f"./text_file/{i}*.txt")
        sentence = ""
        for path in paths:
            with open(path, "r", encoding='utf-8') as f:
                sentence += f.read()
        sentence_list.append(sentence)
    return sentence_list

########################################
# 形態素分解して、1スペースで区切った文章を
# リストに格納する
########################################


def get_corpus_list(sentence_list):
    """文字列を格納したリストを受け取り、形態素ごとに1スペースで区切った文字列に変換して返す関数

    Args:
    sentence_list: list, 
    偉人1人につき、該当するテキストファイル全てから読み込んだ文字列の集合を1要素とするリスト

    Returns:
    corpus_list: list
    引数のリストの各要素において、形態素ごとに1スペースで区切った文字列に変換したリスト
    TODO 本来は、corpusで文章の集合という意味なので、"corpus_list"ではなくcorpusとしたいが、可読性を重視
    """

    # 形態素に分解するAnalyzerをインスタンス化
    # TODO tokenのうち、取り出す品詞を引数で指定して、改良する
    a = Analyzer()
    """Analyzer(char_Filters, tokenizer, token_filters)
    CharFilter のリスト，初期化済み Tokenizer オブジェクト，TokenFilter のリストを指定"""

    # 形態素を（重複含め）格納するリスト
    corpus_list = []
    for sentence in sentence_list:

        corpus = []
        for token in a.analyze(sentence):
            corpus.append(token.surface)

        # joinでスペースに区切って大きな1文にしたあとリストに追加
        corpus = " ".join(corpus)
        corpus_list.append(corpus)

    return corpus_list

#################################
# CountVectorizer とTfidfTransformerの
# コンビを利用して、tfidf値の行列を生成
#################################


def transform_tfidf_array(corpus_list, max_df=0.5, min_df=0):
    """文字列のリストを、tfidf値の行列に変換する関数

    Args: 
    corpus_list: list
    形態素ごとに1スペースで区切った文字列を要素とし、偉人の人数分の要素を格納したリスト

    Returns:
    tfidf_array:numpy.array

    corpus_list: numpy.array
    列に全文章の
    """

    c_vectorizer = CountVectorizer(max_df=max_df, min_df=min_df)
    """CountVectorizer(max_df, min_df)
    TODO max_df, min_dfの値を調整する
    参考偉人#0~5で、max_df設定なしで6746列, max_df=0.5で6083列
    max_df: 頻度が一定以上の単語を捨てる
    min_df: 頻度が一定以下の単語を捨てる"""

    tfidf_transformer = TfidfTransformer()
    X = c_vectorizer.fit_transform(corpus_list)
    tfidf = tfidf_transformer.fit_transform(X)

    # 形式をarrayに変換
    tfidf_array = np.array(tfidf.toarray())
    print(tfidf_array.shape)
    # 全偉人の全文章に含まれる形態素をリストで取得
    feature_names = np.array(c_vectorizer.get_feature_names())

    return tfidf_array, feature_names


"""
c_vectorizer.get_feature_names()
-> 全ての偉人の文章群の形態素のリスト
[...'鳥羽', '鳴らし', '鵜呑み...]

X.toarray()
-> 単語の出現頻度(Bag of Words)
[[ 4  0 32 ...  1  1  0]
 [ 0  0  6 ...  0  0  0]
 [ 6  0 38 ...  0  0  3]
 [ 1  1 25 ...  0  1  0]
 [ 0  0 17 ...  0  0  0]]

tfidf
  (0, 6081)     0.001370677643182339
   ...
  (4, 413)      0.031696372038471546
  (4, 410)      0.031696372038471546
  
tf.idf.toarray()
[[0.         0.00679568 0.00137068 ... 0.00169892 0.00137068 0.        ]
 [0.         0.         0.00845263 ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.01100751]
 [0.00484284 0.         0.         ... 0.         0.00390717 0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]]
  """


def get_word_tfidf_list(tfidf_array, feature_names, ijin_name=0):
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
    vec = tfidf_array[ijin_name]
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


def get_result_file(tfidf_array, feature_names):
    """全偉人分の結果をファイルに出力する関数
    　　　　　　　　開発中の確認のため。
        偉人ごとに、"形態素名: tfidf値"の形式で、tdifd値の降順に結果をファイルに出力する。

    Args: 
    tfidf_array:
    feature_names:

    Returns: なし
    """

    with open("./result/NLP_modeling_出力結果.txt", "w", encoding="utf-8") as f:
        for idx, vec in enumerate(tfidf_array):
            f.write(f"■■■■■■■■■■■■■■■■{idx}人目■■■■■■■■■■■■■■■■■■■■■■■■")
            index = np.argsort(vec)
            words = feature_names[index]
            tfidf = vec[index]
            for i in range(len(vec)):
                f.write(f"{words[-i]} : {tfidf[-i]}\n")


def save_model(file_name, model):
    """引数に名前と対象のモデルを指定し、'ファイル名.json'のタイトルで保存する"""
    with open(file_name + ".binaryfile", "wb") as f:
        pickle.dump(model, f)


if __name__ == "__main__":
    # 全偉人分のモデルを準備
    sentence_list = get_sentence_list(19)
    corpus_list = get_corpus_list(sentence_list)
    tfidf_array, feature_names = transform_tfidf_array(corpus_list)
    # get_result_file(tfidf_array, feature_names) # 開発用：結果をファイル出力

    print(tfidf_array[17])
    # モデル保存を実行
    # save_model("./saved_model/tfidf_array", tfidf_array)
    # save_model("./saved_model/feature_names", feature_names)
