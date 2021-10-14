# 백준 온라인 저지 9297번: Reducing Improper Fractions
# https://www.acmicpc.net/problem/9297

import sys

input = sys.stdin.readline

count = 0

for _ in range(int(input())):
    n1, n2 = map(int, input().split())
    count += 1

    I = n1 // n2
    N = n1 % n2

    if I == 0 and N == 0:
        print("Case %d: %d" % (count, 0))
    elif I == 0:
        print("Case %d: %d/%d" % (count, N, n2))
    elif N == 0:
        print("Case %d: %d" % (count, I))
    else:
        print("Case %d: %d %d/%d" % (count, I, N, n2))
