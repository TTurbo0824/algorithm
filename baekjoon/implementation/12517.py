# 백준 온라인 저지 12517번: Centauri Prime (Small1)
# https://www.acmicpc.net/problem/12517

import sys

input = sys.stdin.readline

# Solution 1

v = ['a', 'e', 'i', 'o', 'u']

for _ in range(1, int(input()) + 1):
    kingdom = input().strip()
    if kingdom[-1] == 'y':
        print('Case #%d: %s is ruled by %s.'%(_, kingdom, 'nobody'))
    elif kingdom[-1] in v:
        print('Case #%d: %s is ruled by %s.'%(_, kingdom, 'a queen'))
    else:
        print('Case #%d: %s is ruled by %s.'%(_, kingdom, 'a king'))

# Solution 2

'''
for i in range(1, int(input()) + 1):
    kingdom = input().strip()
    print('Case #{}: '.format(i)+kingdom+' is ruled by ' + ('nobody.' if kingdom[-1] == 'y' else 'a queen.' if kingdom[-1] in ['a', 'e', 'i', 'o', 'u'] else 'a king.'))
'''