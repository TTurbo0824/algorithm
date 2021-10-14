# 백준 온라인 저지 15651번: N과 M (3)
# https://www.acmicpc.net/problem/15651

from itertools import product
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

p = product(range(1, n + 1), repeat=m)

for i in p:
    for j in i:
        print(j, end=" ")
    print(end="\n")
