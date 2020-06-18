def is_prime(integer):
    """
    与えられた整数が素数かどうかを判定する関数(高速版)
    """
    if integer == 1 or integer == 0:
        return False
    for element in range(2,integer - 50000000):
        if integer % element == 0:
            return False
    return True