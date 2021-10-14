# 백준 온라인 저지 2847번: 게임을 만든 동준이
# https://www.acmicpc.net/problem/2847

score = []
n = int(input())
for _ in range(n):
    score.append(int(input()))

score = score[::-1]

answer = 0

for i in range(1, n):
    if score[i - 1] <= score[i]:
        dif = score[i] - score[i - 1] + 1
        score[i] -= dif
        answer += dif

print(answer)
