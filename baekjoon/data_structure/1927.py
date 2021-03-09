# 백준 온라인 저지 1927번: 최소 힙
# https://www.acmicpc.net/problem/1927 
 
import sys
import heapq

n = int(sys.stdin.readline())
num = []

for _ in range(n):
    temp = int(sys.stdin.readline())
    if temp > 0:
        heapq.heappush(num, temp)
    elif temp == 0:
        if len(num) == 0:
            print(0)
        else:
            print(heapq.heappop(num))