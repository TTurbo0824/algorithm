# 백준 온라인 저지 1159번: 농구 경기
# www.acmicpc.net/problem/1159

import sys

n = int(sys.stdin.readline())

members = {}

for _ in range(n):
    member = sys.stdin.readline().strip()
    if member[0] in members:
        members[member[0]] += 1
    else:
        members[member[0]] = 1

team = []
for member, number in members.items():
    if number >= 5:
        team.append(member)

team.sort()
if team:
    print(*team, sep="")
else:
    print("PREDAJA")
