# 백준 온라인 저지 10872번: 팩토리얼
# https://www.acmicpc.net/problem/10872

def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)

a = int(input())
print(fact(a))