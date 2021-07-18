# 백준 온라인 저지 10698번: Ahmed Aly
# https://www.acmicpc.net/problem/10698

import sys

input = sys.stdin.readline

# Solution 1

for t in range(int(input())):
    eq, ans = map(str, input().rstrip().split('='))
    if eval(eq) == int(ans):
        print("Case %d: YES"%(t + 1))
    else:
        print("Case %d: NO"%(t + 1))

# Solution 2

'''
for t in range(int(input())):
    n, o, m, e, a = map(str, input().rstrip().split())
    n = int(n)
    m = int(m)
    if o == '+':
        k = n + m
    elif o == '-':
        k = n - m
    
    if k == int(a):
        print("Case %d: YES"%(t + 1))
    else:
        print("Case %d: NO"%(t + 1))
'''