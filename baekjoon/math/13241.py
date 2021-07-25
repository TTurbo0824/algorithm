# 백준 온라인 저지 13241번: 최소공배수
# https://www.acmicpc.net/problem/13241

# Solution 1

import math

print(math.lcm(*map(int, input().split())))


# Solution 2

'''
n, m = map(int, input().split())

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return int(a * b / gcd(a, b))

print(lcm(n, m))
'''