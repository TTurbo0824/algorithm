# 백준 온라인 저지 2446번: 별 찍기 - 9
# https://www.acmicpc.net/problem/2446

import sys

n = int(sys.stdin.readline())

for i in range(2 * n - 1): 
    if i < n:
        print(" " * i + "*" * (2 * (n - i) - 1))
    elif i >= n:
        print((n - i % n - 2) * ' ' + "*" * ((i % n + 1) * 2 + 1))