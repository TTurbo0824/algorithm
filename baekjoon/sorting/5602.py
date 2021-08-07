# 백준 온라인 저지 5602번: 問題1
# https://www.acmicpc.net/problem/5602

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

votes = []

lst = [[i, 0] for i in range(m)]

for i in range(n):
    votes.append(list(map(int, input().split())))

for i in range(m):
    for j in range(n):
        lst[i][1] += votes[j][i]
        
lst.sort(key=lambda x: -x[1])

for i, j in lst:
    print(i + 1, end=' ')