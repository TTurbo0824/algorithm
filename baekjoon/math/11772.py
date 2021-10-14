# 백준 온라인 저지 11772번: POT
# https://www.acmicpc.net/problem/11772

import sys

input = sys.stdin.readline

ans = 0

for _ in range(int(input())):
    n = input().strip()
    base = int(n[0:-1])
    exponent = int(n[-1])
    ans += base ** exponent
print(ans)
