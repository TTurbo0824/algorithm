# 백준 온라인 저지 9296번: Grading Exams
# https://www.acmicpc.net/problem/9296

import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    answer = sys.stdin.readline().strip()
    response = sys.stdin.readline().strip()
    score = 0

    for i in range(n):
        if answer[i] != response[i]:
            score += 1

    print("Case %d: %d" % (_ + 1, score))
