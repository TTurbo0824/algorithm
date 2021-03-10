# 백준 온라인 저지 2108번: 통계학
# https://www.acmicpc.net/problem/2108

import sys
input = sys.stdin.readline

from collections import Counter
arr = []

def mean(arr):
    return round(sum(arr)/n)

def median(arr):
    if n == 1:
        return arr[0]
    else:
        return arr[n // 2]

def frequent(arr):
    cnt = Counter(arr)
    if len(arr) == 1:
        return arr[0]
    elif cnt.most_common()[0][1] == cnt.most_common()[1][1]:
        return cnt.most_common()[1][0]
    else:
        return cnt.most_common()[0][0]

def arr_range(arr):
    return arr[-1]-arr[0]

n = int(input())
arr = sorted([int(input()) for _ in range(n)])

print(mean(arr))
print(median(arr))
print(frequent(arr))
print(arr_range(arr))