# 백준 온라인 저지 13484번: Tarifa
# https://www.acmicpc.net/problem/13484

import sys

input = sys.stdin.readline

x = int(input())
n = int(input())

# Solution 1

total = x * (n + 1)

for _ in range(n):
    p = int(input())
    total -= p

print(total)

# Solution 2

"""
p = [int(input()) for _ in range(n)]
print(x * (n + 1) - sum(p))
"""
