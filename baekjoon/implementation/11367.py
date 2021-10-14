# 백준 온라인 저지 11367번: Report Card Time
# https://www.acmicpc.net/problem/11367

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    name, score = map(str, (input().strip().split()))
    score = int(score)
    if 97 <= score <= 100:
        print(name + " A+")
    elif 90 <= score <= 96:
        print(name + " A")
    elif 87 <= score <= 89:
        print(name + " B+")
    elif 80 <= score <= 86:
        print(name + " B")
    elif 77 <= score <= 79:
        print(name + " C+")
    elif 70 <= score <= 76:
        print(name + " C")
    elif 67 <= score <= 69:
        print(name + " D+")
    elif 60 <= score <= 66:
        print(name + " D")
    elif 0 <= score <= 59:
        print(name + " F")
