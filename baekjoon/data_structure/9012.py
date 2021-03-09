# 백준 파이썬 9012번
# https://www.acmicpc.net/problem/9012

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a = list(input())
    s = 0
    for i in a:
        if i == "(":
            s += 1
        elif i == ")":
            s -= 1
        if s < 0:
            print("NO")
            break
    if s > 0:
        print("NO")
    elif s == 0:
        print("YES")