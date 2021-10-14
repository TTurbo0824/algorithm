# 백준 온라인 저지 9610번: 사분면
# https://www.acmicpc.net/problem/9610

import sys

input = sys.stdin.readline

res = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0, "AXIS": 0}

for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        res["AXIS"] += 1
    elif x > 0 and y > 0:
        res["Q1"] += 1
    elif x < 0 and y > 0:
        res["Q2"] += 1
    elif x < 0 and y < 0:
        res["Q3"] += 1
    else:
        res["Q4"] += 1

for key, item in res.items():
    print("%s: %d" % (key, item))
