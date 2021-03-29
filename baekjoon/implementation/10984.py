# 백준 온라인 저지 10984번: 내 학점을 구해줘
# https://www.acmicpc.net/problem/10984

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    credit = 0
    total = 0
    for _ in range(int(input())):
        C, G = map(float, input().split())
        credit += int(C)
        total += C * G
    GPA = total / credit
    print(credit, '%.1f'%GPA)