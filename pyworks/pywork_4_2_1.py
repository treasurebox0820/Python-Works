"""
1. Fibonacci数列をリストで返す関数 make_fib_list を使って数列を100番目まで表示するプログラム
があります。　
このコードはmax_nを100万にするとMemory Error が起こったり、
起動してから入力を受け付けるまでに時間がかかることがわかっています。　
このコードを参考にしてジェネレータを返す関数 gen_fib を作成し、
同じ機能を持ちながら100万を超えるまで安全に表示できるようにプログラムを書き換えてください。
----
"""
def make_fib_list(max_n):
    """先頭からn個のFibonacci数列のリストを返す
    """
    #新しく表示する数の一個前の項がb,二個前の項がaと覚える
    a, b = 0, 1
    """もともと与えられてたやつ。
    ret_list = []
    for _ in range(max_n):
        ret_list.append(b)
        a, b = b, a + b
    return ret_list
    """
    #ジェネレータ式を利用したイテレータを利用
    for _ in range(max_n):
        yield b
        a, b = b, a + b

if __name__ == "__main__":
    max_n = 10000000
    out_s = ""
    for fib_n in make_fib_list(max_n):
        inp = input("次を表示: Enter, 終える: quit > ")
        if inp == "quit": break
        #文字列の形で履歴を作る
        out_s += " " + str(fib_n)
        print(out_s)

