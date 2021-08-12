# 백준 온라인 저지 2720번: 세탁소 사장 동혁 
# https://www.acmicpc.net/problem/2720

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    change = int(input())
    coins = [25, 10, 5, 1]
    ans = [0, 0, 0, 0]

    for coin in coins:
        if change // coin:
            ans[coins.index(coin)] = change // coin
            change %= coin

    print(*ans, sep=' ')