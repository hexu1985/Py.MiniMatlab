#!/usr/bin/env python3
# 离散数学及其应用 （原书第8版）：4.2.3章节，算法5

def binary_expansion(n):
    """
    将十进制整数进行二进制展开
    如果n的二进制展开为(a_{n-1}, ..., a_1, a_0)
    result为[a_0, a_1, ..., a_{n-1}]
    """
    q = n
    k = 0
    result = []
    while (q != 0):
        r = q % 2   # r = q mod 2
        q = q // 2  # q = q div 2
        result.append(r)
    return result

def modular_exponentiation(b, n, m):
    """
    计算b^n mod m
    """
    a = binary_expansion(n)
    x = 1
    power = b % m   # b mod m
    for i in range(len(a)):
        if (a[i] == 1):
            x = (x * power) % m
        power = (power * power) % m
    return x

if __name__ == '__main__':
    for i in range(1, 13):
        print("11**{} mod 13 = {}".format(i, (11**i)%13))
    for i in range(1, 13):
        print("modular_exponentiation(11, {}, 13) = {}".format(i, modular_exponentiation(11, i, 13)))
    print("2^644 mod 645 = ", 2**644%645)
    print("modular_exponentiation(2, 644, 645) = ", modular_exponentiation(2, 644, 645))
