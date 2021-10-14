# 백준 온라인 저지 7785번: 회사에 있는 사람
# https://www.acmicpc.net/problem/7785

import sys

input = sys.stdin.readline

working = {}
for _ in range(int(input())):
    a, b = map(str, input().split())
    if b == "enter":
        working[a] = 1
    elif b == "leave":
        working[a] = 0

answer = []

for people in working:
    if working[people]:
        answer.append(people)

answer.sort(reverse=True)

print(*answer, sep="\n")
