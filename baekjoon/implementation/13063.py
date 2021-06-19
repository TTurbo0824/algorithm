# 백준 온라인 저지 13063번: Lobby
# https://www.acmicpc.net/problem/13063

import sys

input = sys.stdin.readline

while True:
    total, c, r = map(int, input().split())
    
    if (total, c, r) == (0, 0, 0):
        break
    
    if c > total / 2:
        print(0)
    elif r < total / 2:
        print(total // 2 - c + 1)
    elif r >= total / 2:
        print(-1)