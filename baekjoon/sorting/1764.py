# 백준 온라인 저지 1764번: 듣보잡
# https://www.acmicpc.net/problem/1764

import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
answer = []
for i in range(n + m):
    a = input().strip()
    arr.append(a)

result = Counter(arr)

for key, item in result.items():
    if item == 2:
        answer.append(key)

answer.sort()

print(len(answer), *answer, sep="\n")
