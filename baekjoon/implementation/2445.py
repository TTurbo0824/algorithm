# 백준 온라인 저지 2445번: 별 찍기 - 8
# https://www.acmicpc.net/problem/2445

N = int(input())

for i in range(1, N):
    print("*" * i + " " * 2 * (N-i) + "*" * i)
for i in range(N, 0, -1):
    print("*" * i + " " * 2 * (N-i) + "*" * i)