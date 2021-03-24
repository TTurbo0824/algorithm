# 백준 온라인 저지 11047번: 동전 0
# https://www.acmicpc.net/problem/11047

a, b = map(int, input().split())
coin_list = []
num = 0

for i in range(a):
    coin_list.append(int(input()))

coin_list.sort(reverse=True)

for coin in coin_list:
    coin_num = b // coin
    num += coin_num
    b -= coin_num * coin

print(num)