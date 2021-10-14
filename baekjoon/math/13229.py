# 백준 온라인 저지 13229번: Selection Sum
# https://www.acmicpc.net/problem/13229

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(sum(arr[a : b + 1]))
