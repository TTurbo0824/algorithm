# 백준 온라인 저기 2455번: 지능형 기차
# https://www.acmicpc.net/problem/2455

on = []
people = 0

for _ in range(4):
    a, b = map(int, input().split())
    people += b
    people -= a
    on.append(people)

print(max(on))