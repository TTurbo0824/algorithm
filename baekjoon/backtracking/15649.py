# 백준 온라인 저지 15649번: N과 M (1)
# https://www.acmicpc.net/problem/15649

from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

p = permutations(range(1, n), m)

for i in p:
    print(' '.join(map(str, i)))