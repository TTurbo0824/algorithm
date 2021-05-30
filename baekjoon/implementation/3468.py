# 백준 온라인 저지 3468번: Adding Reversed Numbers
# https://www.acmicpc.net/problem/3486

import sys
input = sys.stdin.readline

def newNum(num):
    num = list(num)
    while num[-1] == "0":
        del num[-1]
    return int(''.join(num)[::-1])
        
for _ in range(int(input())):
    n, m = map(str, input().split())
    
    answer = newNum(n) + newNum(m)
    print(newNum(str(answer)))