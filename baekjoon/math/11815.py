# 백준 파이썬 11815번: 짝수? 홀수?
# https://www.acmicpc.net/problem/11815

import sys

input = sys.stdin.readline

t = int(input())

def is_odd_divisor(n):
    if n == int(n ** 0.5) ** 2:
        return 1
    else:
        return 0

nums = list(map(int, input().split()))

for num in nums:
    print(is_odd_divisor(num), end=' ')