import numpy as np
from janome.tokenizer import Tokenizer
import math

def make_list_of_keitaiso(sentence_list):
    """
    引数：
    """
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
    return keitaiso_list

def make_list_of_unique_keitaiso(keitaiso_list):
    unique_keitaiso_list = []
    """

    """

    for words in keitaiso_list:
        for word in words:
            if word not in unique_keitaiso_list:
                unique_keitaiso_list.append(word)
    return unique_keitaiso_list

if __name__ == "__main__":

    with open("nobunaga.txt", "r") as f:
        text_nobunaga = f.read()

    with open("michinaga.txt", "r") as f:
        text_michinaga = f.read()

    with open("saigou.txt", "r") as f:
        text_saigou = f.read()

    sentence_list = [text_nobunaga, text_michinaga, text_saigou]
    print(make_list_of_unique_keitaiso(make_list_of_keitaiso(sentence_list)))
