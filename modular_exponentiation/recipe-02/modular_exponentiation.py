#!/usr/bin/env python3
# 算法概论：1.2.2章节

def modular_exponentiation(b, n, m):
    """
    计算b^n mod m
    """
    if (n == 0): return 1

    z = modular_exponentiation(b, n//2, m)
    if n % 2 == 0:  # n是偶数
        return z**2 % m
    else:
        return x*z**2 % m

if __name__ == '__main__':
    for i in range(1, 13):
        print("11**{} mod 13 = {}".format(i, (11**i)%13))
    for i in range(1, 13):
        print("modular_exponentiation(11, {}, 13) = {}".format(i, modular_exponentiation(11, i, 13)))
    print("2^644 mod 645 = ", 2**644%645)
    print("modular_exponentiation(2, 644, 645) = ", modular_exponentiation(2, 644, 645))
