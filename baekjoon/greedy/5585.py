# 백준 온라인 저지 5585번: 거스름돈
# https://www.acmicpc.net/problem/5585

change = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]

count = 0

for coin in coins:
    if change // coin:
        count += change // coin
        change %= coin

print(count)