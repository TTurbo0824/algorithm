# 백준 온라인 저지 9288번: More Dice
# https://www.acmicpc.net/problem/9288

import sys
input = sys.stdin.readline

# Solution 1

for i in range(int(input())) :
    n = int(input())
    print('Case %d:' % (i + 1))
    for j in range(1, 7) :
        if 1 <= n - j <= 6 and n - j >= j:
            print('(%d, %d)' % (j, n - j))

# Solution2

'''
for i in range(int(input())):
    n = int(input())
    print('Case {}:'.format(i + 1))
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == n and i <= j:
                print('({0},{1})'.format(i, j))
'''