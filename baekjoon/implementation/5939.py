# 백준 온라인 저지 5939번: Race Results
# https://www.acmicpc.net/problem/5939

import sys
input = sys.stdin.readline

score = []

for _ in range(int(input())):
    score.append(list(map(int, input().split())))

score = sorted(score, key = lambda x: (x[0], x[1], x[2]))

for i in score:
    print('%d %d %d'%(i[0], i[1], i[2]))