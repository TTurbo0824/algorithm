# 백준 온라인 저지 2075번: N번째 큰 수
# https://www.acmicpc.net/problem/2075

import heapq
import sys

input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(n):
    nums = list(map(int, input().split()))

    if not heap:
        for num in nums:
            heapq.heappush(heap, num)
    else:
        for num in nums:
            if heap[0] < num:
                heapq.heappush(heap, num)
                heapq.heappop(heap)

print(heap[0])
