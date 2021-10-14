# 백준 온라인 저지 15322번: Košnja
# https://www.acmicpc.net/problem/15322

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    nums = list(map(int, input().split()))
    nums.sort()
    print(2 * (nums[0] - 1))

"""
for _ in range(int(input())):
    n, m = map(int, input().split())
    print((min(n, m)- 1) * 2)
"""
