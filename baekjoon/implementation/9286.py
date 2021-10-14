# 백준 온라인 저지 9286번: Gradabase
# https://www.acmicpc.net/problem/9286

import sys

input = sys.stdin.readline

# Solution 1

"""
answer = []

for t in range(1, int(input()) + 1):
    answer.append(f'Case {t}:')
    for _ in range(int(input())):
        grade = int(input())
        if grade < 6:
            answer.append(grade + 1)

print(*answer, sep='\n')
"""

# Solution 2

answer = ""

for t in range(1, int(input()) + 1):
    answer += f"Case {t}:\n"
    for _ in range(int(input())):
        grade = int(input())
        if grade < 6:
            answer += f"{grade + 1}\n"

print(answer)
