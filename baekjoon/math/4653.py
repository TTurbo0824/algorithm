# 백준 온라인 저지 4653번: Speed Limit
# https://www.acmicpc.net/problem/4635

import sys

input = sys.stdin.readline

while True:
    n = int(input())

    if n == -1:
        break

    lefthour = 0
    answer = 0

    for _ in range(n):
        mph, hour = map(int, input().split())
        answer += mph * (hour - lefthour)
        lefthour = hour

    print("{} miles".format(answer))
    # print(answer, "miles")
