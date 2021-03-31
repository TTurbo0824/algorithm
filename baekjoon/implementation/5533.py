# 백준 온라인 저지 5533번: 유니크
# https://www.acmicpc.net/problem/5533

import sys
input = sys.stdin.readline

N = int(input())

firstgame = []
secondgame = []
thirdgame = []

answer = [0] * N

for _ in range(N):
    first, second, third = map(int, input().split())
    firstgame.append(first)
    secondgame.append(second)
    thirdgame.append(third)

def scoring(arr):
    for i in range(N):
        if arr.count(arr[i]) == 1:
            answer[i] += arr[i]
            
scoring(firstgame)
scoring(secondgame)
scoring(thirdgame)

print(*answer, sep="\n")