# 백준 온라인 저지 15650번: N과 M (2)
# https://www.acmicpc.net/problem/15650

from itertools import combinations
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

p = combinations(range(1, n + 1), m)

for i in p:
    print(" ".join(map(str, i)))
