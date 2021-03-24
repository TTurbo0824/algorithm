# 백준 온라인 저지 11399번: ATM
# https://www.acmicpc.net/problem/11399

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=False)

b = 0
c = 0

for i in range(n):
    b = b + a[i]
    c += b

print(c)