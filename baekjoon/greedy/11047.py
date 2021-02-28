# 백준 온라인 저지 11047번
# https://www.acmicpc.net/problem/11047

a, b = map(int, input().split())
coin = []
num = 0

for i in range(a):
    coin.append(int(input()))

coin.sort(reverse=True)

for i in range(len(coin)):
    if b % coin[i] != b:
        num += b//coin[i]
        b -= b//coin[i] * coin[i]

print(num)