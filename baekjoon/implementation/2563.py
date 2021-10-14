# 백준 온라인 저지 2563번: 색종이
# https://www.acmicpc.net/problem/2563

import sys

input = sys.stdin.readline

n = int(input())
paper = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

answer = 0

for row in paper:
    answer += row.count(1)

print(answer)
