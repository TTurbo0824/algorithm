# 백준 온라인 저지 17010번: Time to Decompress
# https://www.acmicpc.net/problem/17010

import sys

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    a, b = list(map(str, input().split()))
    print(int(a) * b)
