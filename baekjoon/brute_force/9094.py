# 백준 온라인 저지 9094번: 수학적 호기심
# https://www.acmicpc.net/problem/9094
# PyPy3 제출

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    count = 0

    for a in range(1, n - 1):
        for b in range(a + 1, n):
            if (a**2 + b**2 + m) % (a*b) == 0:
                count += 1
    print(count)