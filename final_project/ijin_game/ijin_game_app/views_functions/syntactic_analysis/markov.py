from janome.tokenizer import Tokenizer
import re
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from collections import defaultdict
from collections import Counter
import random

START = '!S!'
END = '!E!'


def scraping():
    """Webスクレイピング

    Returns:
        str: スクレイピングで取得した文字列
    """
    # この勇者が俺ＴＵＥＥＥくせに慎重すぎる
    reading_url = 'https://kakuyomu.jp/works/1177354054881165840/episodes/1177354054881165876'
    html = requests.get(reading_url)
    parse = BeautifulSoup(html.text, 'html.parser')
    parse_tag = parse.find_all('p')

    topics = ""
    for text_data in parse_tag:
        topics += text_data.getText()

    return topics


# print(scraping())


def reg():
    """文字列整形

    スクレイピングで取得した文字列から文章生成に不要な単語や文字列を削除

    Returns:
        str: 整形済み文字列
    """
    text = scraping()
    text = text.replace('閉じる', '')
    text = text.replace('表示設定', '')
    text = text.replace('目次', '')
    text = text.replace('ハートをクリックで、簡単に応援の気持ちを伝えられます。（ログインが必要です）', '')
    text = text.replace('機能をオンにすると、画面の下部をタップする度に自動的にスクロールして読み進められます。', '')
    text = text.replace('…', '')
    text = re.sub(r'一部の.*今はしない', '', text)
    text = re.sub(r'\s', '', text)
    text = re.sub(r'[「」]', '', text)
    # text = text.replace('', '')

    return text


# print(reg())


def sentence(text):
    """文単位に分割

    引数で与えられた文字列を"。"で分割した文リストを作成

    Args:
        text (str): 文字列

    Returns:
        list: 文リスト
    """
    sentences = text.split('。')
    return sentences


# print(sentence(reg()))


def get_three_words_list(sentence):
    """1文を単語3つ1組のタプルに分解する

    Args:
        sentence (str): 文

    Returns:
        list: 文を三分割したリスト
    """
    t = Tokenizer()
    words = t.tokenize(sentence, wakati=True)
    words = [START] + words + [END]
    three_words_list = []

    # print(words)
    # 最後の単語-2まで文を3単語ごとに区切っていく
    # -2するのは最後の単語の1つ前を先頭に3つ区切ろうとすると最後の単語がなくなるから
    # 単語は1語ずつずらしながら3単語のリストを作っていく
    for i in range(len(words) - 2):
        three_words_list.append(tuple(words[i: i + 3]))

    return three_words_list


# print(get_three_words_list('そしてこれまでに五回、地上から勇者を召喚しては困窮する世界を救ってきた'))


def loading(sentences):
    """文章全体を単語3つ1組のタプルにしたリストを作成

    Args:
        sentences (list): 文のリスト

    Returns:
        list: 文章全体を単語3つ1組のタプルにしたリスト
    """
    three_words_list = []
    for sentence in tqdm(sentences):
        three_words_list += get_three_words_list(sentence)
    return three_words_list


# print(loading(sentence(reg())))
# print(Counter(loading(sentence(reg()))))


def generate_markov_dict(three_words_count):
    """マルコフ連鎖の辞書を生成

    最初の2語から次の1語を導く。導き方は重さ。

    Args:
        three_words_count (Counter): 3単語1組のタプルとその出現回数の辞書

    Returns:
        dict: マルコフ辞書
    """
    markov_dict = {}
    for three_words, count in three_words_count.items():
        two_words = three_words[:2]  # 最初の2単語
        next_word = three_words[2]  # 最後の単語
        if two_words not in markov_dict:
            markov_dict[two_words] = {'words': [], 'weights': []}
        markov_dict[two_words]['words'].append(next_word)  # 最初の2語と近い次の1語
        markov_dict[two_words]['weights'].append(count)  # 最初の2語と近い次の1語の重さ
    return markov_dict


# print(generate_markov_dict(Counter(loading(sentence(reg())))))


def get_first_words_weights(three_words_count):
    """最初にどの単語を選ぶのかを決定する

    STARTマーキングの次の単語を最初の1語の候補とする。

    Args:
        three_words_count (Counter): 3単語1組のタプルとその出現回数の辞書

    Returns:
        tuple: (最初の1語となる単語リスト, 最初の1語となる単語の出現回数(重さ)リスト)
    """
    first_word_count = defaultdict(int)
    for three_words, count in three_words_count.items():
        if three_words[0] == START:
            next_word = three_words[1]
            first_word_count[next_word] += count

    words = []
    weights = []
    for word, count in first_word_count.items():
        words.append(word)
        weights.append(count)

    return words, weights


def generate_text(fwords, fweights, markov_dict):
    """文章を生成

    Args:
        fwords (list): 単語リスト
        fweights (list): 単語の重さリスト
        markov_dict (dict)): マルコフ辞書

    Returns:
        str: 生成された文章
    """
    first_word = random.choices(fwords, weights=fweights)[0]
    generate_words = [START, first_word]
    while True:
        pair = tuple(generate_words[-2:])
        words = markov_dict[pair]['words']
        weights = markov_dict[pair]['weights']
        next_word = random.choices(words, weights=weights)[0]
        if next_word == END:
            break
        generate_words.append(next_word)

    return ''.join(generate_words[1:])


def main():
    """文章自動生成実行
    """
    base_text = reg()  # 整形済みの文章全体
    sentences = sentence(base_text)  # 1文ごとのまとまりのリスト
    tw_list = loading(sentences)  # 1文を単語3つ1組のタプルに分解したリスト
    # 各3単語1組のタプルがいくつ出現したかカウントした辞書。3単語1組が完全一致する場合にカウントアップ
    cnt = Counter(tw_list)
    markov_dict = generate_markov_dict(cnt)    # マルコフ連鎖の辞書
    first_words_weights = get_first_words_weights(cnt)
    gen_text = generate_text(*first_words_weights, markov_dict)
    return gen_text


# main()


def test():
    """処理理解用テスト関数"""
    tw_list = loading(["今日はいい天気です", "明日は曇りみたいです", "明後日は雨かもしれません"])
    cnt = Counter(tw_list)
    markov_dict = generate_markov_dict(cnt)
    first_words_weights = get_first_words_weights(cnt)
    gen_text = generate_text(*first_words_weights, markov_dict)
    print(tw_list, '\n')
    print(cnt, '\n')
    print(markov_dict, '\n')
    print(first_words_weights, '\n')
    print(gen_text)


# test()
