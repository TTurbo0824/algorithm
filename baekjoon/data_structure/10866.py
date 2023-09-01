# 백준 온라인 저지 10866번: 덱
# https://www.acmicpc.net/problem/10866

import sys

n = int(input())
deque = []

for _ in range(n):
    a = sys.stdin.readline().split()    
    if a[0] == "push_front":
        deque.insert(0, a[1])
    elif a[0] == "push_back":
        deque.append(a[1])
    elif a[0] == "pop_front":
        if len(deque) != 0:
            print(deque.pop(0))
        else:
            print(-1)
    elif a[0] == "pop_back":
        if len(deque) != 0:
            print(deque.pop(-1))
        else:
            print(-1)
    elif a[0] == "size":
        print(len(deque))
    elif a[0] == "empty":
        if len(deque) != 0:
            print(0)
        else:
            print(1)
    elif a[0] == "front":
        if len(deque) != 0:
            print(deque[0])
        else:
            print(-1)
    elif a[0] == "back":
        if len(deque) != 0:
            print(deque[-1])
        else:
            print(-1)