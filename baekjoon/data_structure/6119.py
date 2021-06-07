# 백준 온라인 저지 6119번: Cow Line
# https://www.acmicpc.net/problem/6119

# Solution 1

import sys
from collections import deque

input = sys.stdin.readline

cards = deque()
card = 1

for i in range(int(input())):
    command = list(map(str, input().split()))
    
    if command[0] == "A" and command[1] == "L":
        cards.appendleft(card)
        card += 1
    elif command[0] == "A" and command[1] == "R":
        cards.append(card)
        card += 1
    elif command[0] == "D" and command[1] == "L":
        for _ in range(int(command[2])):
            cards.popleft()
    elif command[0] == "D" and command[1] == "R":
        for _ in range(int(command[2])):
            cards.pop()
    
print(*cards, sep="\n")

# Solution 2

'''
import sys

input = sys.stdin.readline

cards = []
card = 1

for _ in range(int(input())):
    command = list(map(str, input().split()))
    
    if parameter == "A" and command[1] == "L":
        cards.insert(0, card)
        card += 1
    elif parameter == "A" and command[1] == "R":
        cards.append(card)
        card += 1
    elif parameter == "D" and command[1] == "L":
        cards = cards[int(command[2]):len(cards)]
    elif parameter == "D" and command[1] == "R":
        cards = cards[0:len(cards) - int(command[2])]

print(*cards, sep="\n")
'''