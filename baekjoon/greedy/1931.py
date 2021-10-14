# 백준 온라인 저지 1931번: 회의실 배정
# https://www.acmicpc.net/problem/1931

import sys

n = int(input())
time = []

for i in range(n):
    time.append(list(map(int, sys.stdin.readline().split())))

time = sorted(time, key=lambda x: (x[1], x[0]))
num = 1

end_time = time[0][1]

for i in range(1, n):
    if time[i][0] >= end_time:
        num += 1
        end_time = time[i][1]

print(num)
