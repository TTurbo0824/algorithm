# 백준 온라인 저지 2530번: 인공지능 시계
# https://www.acmicpc.net/problem/2530

import sys

input = sys.stdin.readline

hour, minute, second = map(int, input().split())
n = int(input())

second += n

if second >= 60:
    minute += second // 60
    second %= 60

if minute >= 60:
    hour += minute // 60
    minute %= 60

if hour >= 24:
    hour %= 24

print(hour, minute, second)
