"""
問題//////////////////////////////////////////////////////////////////
任意の関数の実行時間を測定するデコレータ関数を作成し、
実行に一定の時間がかかる関数を作成して関数の実行時間を測定してください。
（ヒント：time モジュールの time, time_ns, sleep など）



"""
import time as t

def waste_your_time(x):
    """
    引数の秒数を経過してから、文章を表示する関数
    """
    t.sleep(x)
    return print(f"{x}秒無駄にしました")

def add_time_measuring_function(func):
    """
    デコレーター
    """
    def wrapper(*args,**kwargs):
        t1 = t.time()
        result = func(*args,**kwargs)
        t2 = t.time()
        print(f"関数の実行から終了までの時間は、{t2-t1}")
        return result
    return wrapper



if __name__ == "__main__":
    #decolated_func = add_time_measuring_function(waste_your_time)
    #decolated_func(5)
    add_time_measuring_function(waste_your_time)(5)

