"""
（時間が余ったら）①4の問題の is_prime を使って 100,000,000 （１億）
から 100,000,100 （１億100）までの範囲に含まれる全ての素数とその個数を表示してください。
②そのプログラムに time モジュールの 適切なメソッドを使って、計算にかかる時間を測定してください。
それが済んだら、③計算時間を短くするための工夫を一つ加えたプログラムを作成し、
計算時間が短くなることを実証してください。
"""
from pywork_prime2 import is_prime
import time
#処理前の時刻
t1 = time.time()

#素数を入れいていくprime_list
prime_list = []

#一億～一億百までの素数チェック
n = 100000000
while n <= 100000100:
    if is_prime(n):
        prime_list.append(n)
    n += 1

#処理後の時刻
t2 = time.time()
print("素数のリストは下記のようになります。\n{}\n素数の個数は{}個です。".format(prime_list,len(prime_list)))
elapsed_time=t2 - t1
print("経過時間は",elapsed_time)