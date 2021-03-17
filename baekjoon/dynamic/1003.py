# 백준 온라인 저지 1003번: 피보나치 함수
# https://www.acmicpc.net/problem/1003

t = int(input())

for _ in range(t):
    n = int(input())
    k = n - 1
    a, b = 0, 1

    while k > 0:
        a, b = b, a + b
        k -= 1

    if n == 0:
        print(1, 0)
    else:
        print(a, b)