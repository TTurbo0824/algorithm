# 백준 온라인 저지 2702번: 초6 수학
# https://www.acmicpc.net/problem/2702

import math

# Solution 1
# Python 3.9 이하 버전

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(lcm(n, m), end=' ')
    print(math.gcd(n, m))

# Solution 2

'''
for _ in range(int(input())):
    n, m = map(int, input().split())
    print(math.lcm(n, m), end=' ')
    print(math.gcd(n, m))
'''