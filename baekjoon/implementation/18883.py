# 백준 온라인 저지 18883번: N M 찍기
# https://www.acmicpc.net/problem/18883

n, m = map(int, input().split())
k = n * m

for i in range(1, k + 1):
    if i % m == 0:
        print(i)
    else:
        print(i, end=" ")
