"""
itemsは辞書をリストに変える
"""


sent="""
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
"""
#文字を格納する辞書を作っておく
count_dict={}
#sentから一文字づつ取り出して、count_dictに入ってなかったら新たに要素をつくり、
#入ってたら１増やす
for letter in sent:
    if letter in count_dict:
        count_dict[letter]+=1
    else:
        count_dict[letter]=1

print(count_dict)
print(count_dict.items[1])





"""
letter2 = ango_dic.get(letter,letter)
これはletterがango_dicに入っていたら、valueを取得し、入ってなかったら二個目の引数を取得
"""

  
