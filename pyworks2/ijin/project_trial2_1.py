# -*- coding: utf-8 -*-
import numpy as np

with open("nobunaga.txt", "r") as f:
    text_nobunaga = f.read()

with open("michinaga.txt", "r") as f:
    text_michinaga = f.read()

with open("saigou.txt", "r") as f:
    text_saigou = f.read()

 

# 単語を特徴量ベクトルBag of Wordsに変換
from janome.tokenizer import Tokenizer
import math

##文章を形態素の要素ごとに、リストに格納する
sentence_list = [text_nobunaga, text_michinaga, text_saigou]#この時点では形態素にわかれてなくない？

# 形態素解析をするトークンtokenizerを生成！
tokenizer = Tokenizer()

# 形態素を（重複含め）格納するリスト
keitaiso_list = []
for text_element in sentence_list:
    
    # tokenのうち、品詞が●●のもののみ追加
    #ここの文章を使うこと、keitiso_listが入れ子型の構造になる
    #text_elementは一つ一つの文章全体。それをtokenizer.tokenizeで形態素分解されたリストがでてくる。
    #名詞だけここで選ばれるようにtoken.part_of_speech.starwith("名詞でしている")
    A = [token.surface for token in tokenizer.tokenize(text_element) if token.part_of_speech.startswith("名詞")]

    #
    keitaiso_list.append(A) 

"""各形態素の品詞を確認するために、テキストデータに書きだしするためのコード"""
# with open("hinshi_kakunin_all.txt", "w") as f:
#     for i in keitaiso_list:
#         f.write(f"{i}")
#         f.write("\n")
        

#print("形態素リスト*****keitaiso_list**********************\n", keitaiso_list, "*********")

##重複したワードを削除する###################################
unique_keitaiso_list = []
"""keitaiso_list:  [[文章1の形態素の配列][文章2の形態素の配列]...]"""

for words in keitaiso_list:
    for word in words:
        if word not in unique_keitaiso_list:
            unique_keitaiso_list.append(word)

#print("形態素リスト***(unique_keitaiso_list)************************\n",unique_keitaiso_list)
"""
形態素リスト（重複なし）：
 ['今日', 'の', '天気', 'は', '良い', 'です', '明日', '雨', 'よう', '明後日', 'くもり', 'かも', 'しれ', 'ませ', 'ん']
"""


##各単語が文章中に何回出たか(TF) を文章ごとに
"""
bow_list
 [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 2, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
"""###########################

#
bow_list = []

# words = 形態素に分解された文章
for words in keitaiso_list:
    bow = []

    # unique = "今日" "の"...ユニークの形態素の要素
    # uniqueに入ってる順番でbowを作る。keitaiso_listの１要素wordsの中を調べて、ユニークの中に入ってる言葉の数を数える。
    for unique in unique_keitaiso_list:
        bow.append(words.count(unique))
    #ここでも入れ子型。
    bow_list.append(bow)
#print(bow_list)


## idfを算出########################################
# idfは一個の
# words_count  = 形態素の要素数（重複あり）の数
words_count = len(keitaiso_list) # len(keitaiso_list)は文章の数を表す。4/27現在３つ
idf_list = []

# ユニーク形態素の数の分、for文を回す
for i in range(len(unique_keitaiso_list)):#unique_keitaiso_listは全部の文章の形態素がはいったリスト

    # 毎回countを0に初期化
    count = 0

    # 出現回数の数のリスト
    # ★bow_list★: 
    # '今日', 'の', '天気', 'は', '良い', 'です', '明日', '雨', 'よう', '明後日', 'くもり', 'かも', 'しれ', 'ませ', 'ん'
    # [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 2, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
    ###新登場のワードはどんどん後ろについかされていく。


    # 各行で、1列目の値が1以上の場合、count+=1する
    #ここなおしたけどもしかして西郷さんだけにここで絞ってる？
    for bows in bow_list:#それぞれの文章のbowについて
        if bows[i] > 0:###ここをbowからbowsに直した。bowだと前のfor文の一番最後のbowになってしまう。
            count += 1### このcountは何を表しているの？


    #words_countは文章の数4/27時点では３。countは
    idf_list.append(round(math.log((words_count + 1) / ( count + 1)), 5))#roundの第二引数は小数点の位を指定
    #print("甘く、長い、口づけをかわそう、深く限りなくあなたを知りたい",idf_list)




## 特徴量(tf*idf)をもとめる#########################################

# bow_listの1つ目の文章について考える
###ここでは文章を大きな塊としてみている。
bow_data = bow_list[0]

word_summary = sum(bow_data)###全部の文章に出てくる、名詞をすべて足した数

tfidf_list = []

for i, value in enumerate(bow_data):
    
    # ＴＦ: 出現割合
    # 
    # その文章の中で「今日」が出現する回数　÷ この文章に含まれる形態素数
    tf = value / word_summary
    # 例）1 / (1 + 1 + 2 + 1 + 1 + 1)
    # 1つ目の文章についての　tf = [1/7, 1/7, 2/7, 1/7, 1/7, 1/7, 0,0,0,....0,0]


    # ＴＦ・ＩＤＦ値を求める
    # ＩＤＦ値　= その文章の中で「今日」が出現する回数
    tfidf_list.append(round(tf * (idf_list[i] + 1), 5))#ここで１を足すのがよくわからない。


"""numpyでプリントの設定を行い、有効桁数などを設定"""
np.set_printoptions(threshold=np.inf) # スレッド数の上限は「無限」
np.set_printoptions(precision=4, suppress=True) # 有効桁数 (常にこうしたい場合のみ)


#print("★各形態素のTF・IDF値***********\n", tfidf_list)
#print(len(unique_keitaiso_list))
#print(len(tfidf_list))


""" {形態素: tfidf値}　の辞書にする
　　例）...('藤原', 0.0167), ('兼', 0.01778),...　"""

# 辞書にする
#unique_keitaiso_listの形態素とtfidf_listの数値は対応している
keitaiso_tfidf_dict = {key: val for key, val in zip(unique_keitaiso_list, tfidf_list)}

# 辞書を値tfidfで降順に並び替えてタプル化
keitaiso_tfidf_list = sorted(keitaiso_tfidf_dict.items(), key=lambda x:x[1], reverse = True)

# tfidf値が0の要素を取り除いたタプルにする
keitaiso_tfidf_list_0_remove =  [i for i in keitaiso_tfidf_list if i[1] != 0.0]
print(keitaiso_tfidf_list)


# tfidfの合計値
total = 0
for set_ in keitaiso_tfidf_list_0_remove:
    total += set_[1]
print("該当文章の全単語のtfidf値の合計：", total)




# スコア算出######################################################

"""入力の文章を自分で作る"""
# input_text = "藤原道長は、摂政と関白を歴任した。御堂殿と呼ばれている。娘の彰子は後一条天皇のもとに嫁がせ、外戚として権力を振るった。"
input_text = "信長は尾張の国の領主。桶狭間の戦いで今川を破った。娘を嫁がせた。斎藤道三と結んだ"
# input_text = "西郷は、鹿児島県出身の下級武士。幕末。薩長同盟を成立させた。軍の参謀。西南戦争で死亡。"

score = 0
# 入力を形態素に分解してリスト化
input_keitaiso_list = tokenizer.tokenize(input_text, wakati = True)

# uniqueの集合にする
input_keitaiso_set = set(input_keitaiso_list)
#print("入力された文章に含まれる形態素のリスト：", input_keitaiso_set)
#print("*"*20)

# スコア算出（途中）
# 入力された文章の形態素をfor文で回し、教師データに含まれている単語だった場合は、tf*idfの値を出力する
"""まだ途中、どのようにスコア化するか、？？？？
スコア算出の基準の例：
１．重要キーワードが入っていれば、70点ぐらいになるようにする（上位20単語）
２．70点以上のキーワードがあればあるほど、100点に近づく
"""

for keitaiso in input_keitaiso_set:

    for element in keitaiso_tfidf_list_0_remove:
        if keitaiso in element:

            # その形態素のtfidf
            #print(element[1],element[0])
            3+2
            # その形態素

    # elif keitaiso in keitaiso_tfidf_list_0_remove:
    #     print(keitaiso)
    #     score += 1
    #     print("*"*20)

    # elif keitaiso in keitaiso_tfidf_list_0_remove:
    #     print(keitaiso)
    #     score += 0.1
    #     print("*"*20)
    # print(score)



"""【失敗】配列を縦に結合する
np.array([配列A, 配列B])・・・×
np.append([配列A, 配列B])　・・・×
配列Bが文字列型になってしまった・・・結局うまくいかず"""


"""numpy array配列を特定の行や列を基準にソートする
ステップ１）np.argsort(配列Ａ) # 配列Ａを並び替えた”インデックス”を返す
ステップ２）そのインデックスを並び替えたい配列Ｂに適応 arrayB[np.argsort(配列Ａ）)]

....【失敗】 TFIDFのfloat型配列と、形態素のstr型の配列をつくり、
　　　tfidfの大きさの順で、形態素の配列をソートするのが失敗。

tfidf_list_casted = np.array(tfidf_list, dtype=float)

# 順番のインデックスを取得する
order_index = np.argsort(tfidf_list_casted)

# 並び替え
tfidf_list_casted_ordered = tfidf_list_casted[order_index]
print(tfidf_list_casted_ordered)
unique_keitaiso_list_ordered = unique_keitaiso_list[order_index]
"""


"""
#idfについて




"""
print(keitaiso_tfidf_list_0_remove)