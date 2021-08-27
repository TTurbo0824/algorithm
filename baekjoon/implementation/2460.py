# 백준 온라인 저지 2460번: 지능형 기차 2
# https://www.acmicpc.net/problem/2460

a = 0
b = []

for i in range(10):
    x, y = map(input().split())
    a = a - x + y
    b.append(a)

print(max(b))