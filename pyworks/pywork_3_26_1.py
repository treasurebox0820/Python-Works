def calc_power(x,y):
	"""xのy乗を計算する"""
	result = x **y
	return result
print(calc_power(2,10))

def show_args(*args):
	"""位置引数のタプル化の例"""
	print("Positional args:",args)
	return args
show_args("a","b","c","d","e","f")

def show_kwargs(**kwargs):
	"""キーワード引数の辞書化の例"""
	print("Keyword args:", kwargs)
	return kwargs
show_kwargs(a="パスタ", b="赤ワイン", c="肉料理")

animal = "cat"
print("animal in global:",animal)
def my_func():
	vegetable = "carot"
	print("animal      in my_func:",animal)
	print("vegetable   in my_func:",animal)

my_func()
#print("vegetable:", vegetable)

animal = "cat"
print("animal in global:", animal)
def my_func():
	global animal
	animal = "dog"
	print("animal in my_fucn()", animal)
my_func()
print("animal global after my_func:", animal)


def print_upto(num):
    """与えられた数未満の数を表示"""
    num_str=""
    for i in range (num):
        #
	    num_str = ""+ str(i)
	    print(num_str)

if __name__== "__main__":
	print_upto(10)