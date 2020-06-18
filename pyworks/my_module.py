def print_upto(num):
    """与えられた数未満の数を表示"""
    num_str = ""
    for i in range (num):
        num_str += ""+ str(i)
    print(num_str)

if __name__ == "__main__":
    print_upto(10)


