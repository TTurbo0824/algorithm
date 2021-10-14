# 백준 온라인 저지 13771번: Presents
# https://www.acmicpc.net/problem/13771

import sys

input = sys.stdin.readline

presents = []

for _ in range(int(input())):
    presents.append(float(input()))

presents.sort()
print("%.2f" % presents[1])
