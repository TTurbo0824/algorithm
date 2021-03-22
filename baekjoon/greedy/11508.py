# 백준 온라인 저지 11508번: 2+1 세일
# https://www.acmicpc.net/problem/11508

import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)

total = 0

for i in range(N):
    if i % 3 != 2:
        total += arr[i]
        
print(total)