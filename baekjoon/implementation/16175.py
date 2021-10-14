# 백준 온라인 저지 16175번: General Election
# https://www.acmicpc.net/problem/16175

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())

    total = []
    candidates = [0] * n

    for _ in range(m):
        votes = list(map(int, input().split()))
        total.append(votes)

    for i in range(m):
        for j in range(n):
            candidates[j] += total[i][j]

    print(candidates.index(max(candidates)) + 1)
