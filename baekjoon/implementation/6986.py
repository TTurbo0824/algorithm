# 백준 온라인 저지 6986번: 절사 평균
# https://www.acmicpc.net/problem/6986

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

score = []

for _ in range(N):
    score.append(float(input()) * 10)

score.sort()
new = score[K : N - K]

trimmed = sum(new) / (N - 2 * K) / 10
adjusted = (sum(new) + new[0] * K + new[-1] * K) / (N * 10)

print("%.2f" % (trimmed + 0.0000000001))
print("%.2f" % (adjusted + 0.0000000001))
