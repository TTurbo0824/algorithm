# 백준 온라인 저지 2164번
# https://www.acmicpc.net/problem/2164

import collections

n = int(input())
cards_deque = collections.deque([i for i in range(1, n + 1)])

while len(cards_deque) != 1:
    cards_deque.popleft()
    cards_deque.rotate(-1)

print(cards_deque[0])