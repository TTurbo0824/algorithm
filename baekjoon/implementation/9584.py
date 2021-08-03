# 백준 온라인 저지 9584번: Fraud Busters
# https://www.acmicpc.net/problem/9584

import sys

input = sys.stdin.readline

code = input().strip()
answer = []

for t in range(int(input())):
    plate = input().strip()
    isMatching = True
    
    for c, p in zip(code, plate):
        if c != "*" and c != p:
            isMatching = False
            break

    if isMatching == True:
        answer.append(plate)
        
print(len(answer))
print(*answer, sep="\n")