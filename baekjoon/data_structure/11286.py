# 백준 온라인 저지 11286번: 절댓값 힙
# https://www.acmicpc.net/problem/11286

import sys
import heapq

n = int(sys.stdin.readline())
num = []

for _ in range(n):
    temp = int(sys.stdin.readline())
    if temp != 0:
        heapq.heappush(num, (abs(temp), temp))
    elif temp == 0:
        if len(num) == 0:
            print(0)
        else:
            print(heapq.heappop(num)[1])
