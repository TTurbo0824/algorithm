# 백준 온라인 저지 16953번: A → B
# https://www.acmicpc.net/problem/16953

from collections import deque

A, B = map(int, input().split())

answer = -1

queue = deque([(A, 1)])

while queue:
    current, count = queue.popleft()
    if current == B:
        answer = count
        break
    if current * 2 <= B:
        queue.append((current * 2, count + 1))
    if current * 10 + 1 <= B:
        queue.append((current * 10 + 1, count + 1))

print(answer)
