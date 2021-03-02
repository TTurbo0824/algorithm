# 백준 온라인 저지 1946번
# https://www.acmicpc.net/problem/1946

import sys

T = int(input())

for _ in range(T):
    N = int(input())
    count = 1
    people = []

    for i in range(0, N):
        Paper, Interview = map(int, sys.stdin.readline().split())
        people.append([Paper, Interview])
    
    people = sorted(people, key=lambda x: x[0])

    best = people[0][1]

    for i in range(1, N):
        if best > people[i][1]:
            count += 1
            best = people[i][1]

    print(count)