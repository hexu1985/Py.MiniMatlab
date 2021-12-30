#!/usr/bin/env python3

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

if __name__ == '__main__':
    test_list = [12345, 177130, 241]
    for i in test_list:
        print(i, ":", bin(i))
        blist = binary_expansion(i)
        blist.reverse()
        print(blist)

