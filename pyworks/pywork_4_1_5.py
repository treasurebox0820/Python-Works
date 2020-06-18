"""
【ワーク 4-4：関数で繰り返し】
1.１から１０までの数字をおのおの２乗した和を計算するプログラムを for文で作成してください。
2.上記のプログラムを while 文で作成してください。
3.上記のプログラムを for文や while文を使わず、関数を使って作成してください。
（標準取組時間 １時間）


再帰
"""
#1
total_for = 0
for i in range(1,11):
    i_square = i**2
    total_for += i_square
print(f"合計は{total_for}")

#2
total_while = 0
for i in range(1,11):
    i_square_while = i**2
    total_while += i_square_while
print(f"合計は{total_while}")

#3
list_square = [x**2 for x in range(1,11) ]
print("合計は{}".format(sum(list_square)))

#4
print(sum(list(map(lambda x:x**2, range(1,11)))))

#5

def square_function(n,total):
    if n == 0:
        return total
    else:
        total += n**2
        return square_function(n-1,total)

square_function(10,0)

def square_function3(n):
    if n <= 0:
        return 0
    return square_function3(n-1) + n**2




print(square_function3(10))