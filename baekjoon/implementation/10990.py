# 백준 온라인 저지 10990번: 별 찍기 - 15
# https://www.acmicpc.net/problem/10990

N = int(input())

for i in range(1, N + 1):
    if i == 1:
        print(" " * (N - 1) + "*")
    else:
        print((N - i) * " " + "*" + " " * ((i - 2) * 2 + 1) + "*")