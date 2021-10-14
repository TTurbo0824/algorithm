# 백준 온라인 저지 9947번: Coin tossing
# https://www.acmicpc.net/problem/9947

import sys

input = sys.stdin.readline

while True:
    p1, p2 = map(str, input().strip().split())

    if p1 == p2 == "#":
        break

    s1 = s2 = 0

    for _ in range(int(input())):
        c, r = map(str, input().strip().split())
        if c == r:
            s1 += 1
        else:
            s2 += 1

    print(p1, s1, p2, s2, sep=" ")
