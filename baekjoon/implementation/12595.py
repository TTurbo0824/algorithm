# 백준 온라인 저지 12595번: Odd Man Out (Small)
# https://www.acmicpc.net/problem/12595

import sys

input = sys.stdin.readline

count = 0

for _ in range(int(input())):
    n = int(input())
    guests = list(map(int, input().split()))
    for person in guests:
        if guests.count(person) == 1:
            count += 1
            print("Case #%d: %d" % (count, person))
