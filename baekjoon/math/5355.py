# 백준 온라인 저지 5355번: 화성 수학
# https://www.acmicpc.net/problem/5355

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, *arr = map(str, input().strip().split())
    n = float(n)

    for el in arr:
        if el == "#":
            n -= 7
        if el == "%":
            n += 5
        if el == "@":
            n *= 3

    print(format(n, ".2f"))
