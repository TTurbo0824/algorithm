# 백준 온라인 저지 2506번: 점수계산
# https://www.acmicpc.net/problem/2506

import sys

input = sys.stdin.readline

n = int(input())
score = list(map(int, input().split()))

count = 0
ans = 0

for s in score:
    if s == 1:
        count += 1
        ans += count
    else:
        count = 0

print(ans)
