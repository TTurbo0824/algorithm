# 백준 온라인 저지 13772번: Holes
# https://www.acmicpc.net/problem/13772

import sys

input = sys.stdin.readline

holes = {"A": 1, "B": 2, "D": 1, "O": 1, "P": 1, "Q": 1, "R": 1}

for _ in range(int(input())):
    line = input().strip()
    answer = 0

    for letter in line:
        if letter in holes.keys():
            answer += holes[letter]

    print(answer)

"""
for _ in range(int(input())):
    line = input()
    print(sum(map(lambda t: line.count(t), 'ADOPQR')) + 2 * line.count('B'))
"""
