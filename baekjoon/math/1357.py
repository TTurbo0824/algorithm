# 백준 온라인 저지 1357번: 뒤집힌 덧셈
# https://www.acmicpc.net/problem/1357

x, y = input().split()
s = int(x[::-1]) + int(y[::-1])
result = str(s)[::-1]

print(int(result))