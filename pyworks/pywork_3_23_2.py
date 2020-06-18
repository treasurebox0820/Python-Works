"""
問題
3.for文を使って1から50までの数字を表示してください。ただし、数字が 3の倍数なら Fizz、
5の倍数なら Buzz、 3 と 5 のいずれの倍数でもあるなら FizzBuzz と表示してください。

美しく表示したい＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠


美しく表示したい＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠

制作手順＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠
1.for文で５０までの数字がならぶ反復子を作る
2.先に３かつ５で割り切れる（１５と書いてもいいかも）のときにFBと出力とかく
3.つぎに３、つぎに５（ここは順番かんけいない）
4.あとはなんのもひっかからなかったものはそのまま数字を書くようにする
制作手順＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠



"""
for i in range(51):
    if i%3==0 and i%5==0:
        print("FizzBuzz",end=",\n",)
    
    elif i%3==0:
        print("Fizz",end=",\n")
    elif i%5==0:
        print("Buzz",end=",\n")
    else:
        print(i,end=",  ")


for i in range(51):
    if i%3==0 and i%5==0:
        print("FizzBuzz",end=",　　",)
    
    elif i%3==0:
        print("Fizz",end=",　　")
    elif i%5==0:
        print("Buzz",end=",　　")
    else:
        print(i,end=",  ")
    if i%10 == 0:
        print("\n")



"""
rangeの確認
print(list(range(51)))
"""