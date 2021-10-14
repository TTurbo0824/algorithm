# 백준 온라인 저지 9713번: Sum of Odd Sequence
# https://www.acmicpc.net/problem/9713

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    print(((n // 2) + 1) ** 2)
