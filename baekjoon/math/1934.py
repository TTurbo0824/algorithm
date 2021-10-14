# 백준 온라인 저지 1934번: 최소공배수
# https://www.acmicpc.net/problem/1934


def gcd(A, B):
    if B % A:
        return gcd(B % A, A)
    else:
        return A


def lcm(A, B):
    return int((A * B) / gcd(A, B))


T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    print(lcm(A, B))
