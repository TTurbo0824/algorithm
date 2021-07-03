# 백준 온라인 저지 5919번: Hay Bales
# https://www.acmicpc.net/problem/5919

import sys

input = sys.stdin.readline

n = int(input())
hay = [int(input()) for _ in range(n)]
avg = sum(hay) // n

answer = 0

for h in hay:
    answer += abs(avg - h)

print(answer // 2)