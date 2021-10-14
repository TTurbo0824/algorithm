# 백준 온라인 저지 : Olympic Games
# https://www.acmicpc.net/problem/13773

import sys

input = sys.stdin.readline

while True:
    n = int(input())

    if n == 0:
        break

    if n < 1896 or n % 4 != 0:
        print("%d No summer games" % n)
    elif n % 4 == 0:
        if 1914 <= n <= 1918 or 1939 <= n <= 1945:
            print("%d Games cancelled" % n)
        elif n > 2020:
            print("%d No city yet chosen" % n)
        else:
            print("%d Summer Olympics" % n)
