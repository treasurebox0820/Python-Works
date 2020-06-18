"""
与えられた整数が素数かどうかを判定する関数 is_prime を作ってください。
それを使って1から100までの範囲に含まれる全ての素数とその個数を表示してください。
素数とは、その数自身と１以外の数で割り切れない正の整数のことです。
"""
from pywork_prime import is_prime

#素数を格納するprime_list
prime_list = []
n = 0
while n <= 100:
    if is_prime(n):
        prime_list.append(n)
    n+=1
print("素数のリストは下記のようになります。\n{}\n素数の個数は{}個です。".format(prime_list,len(prime_list)))