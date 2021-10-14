# 백준 온라인 저지 5635번: 생일
# https://www.acmicpc.net/problem/5635

import sys

n = int(sys.stdin.readline())

arr = []

for _ in range(n):
    data = 0
    name, d, m, y = list(map(str, sys.stdin.readline().strip().split(" ")))
    if len(d) == 1:
        d = "0" + d
    if len(m) == 1:
        m = "0" + m
    arr.append((name, y + m + d))

arr = sorted(arr, key=lambda x: int(x[1]))
print(arr[-1][0])
print(arr[0][0])
