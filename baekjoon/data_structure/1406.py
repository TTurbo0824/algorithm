# 백준 온라인 저지 1158번
# https://www.acmicpc.net/problem/1406

import sys

s1 = []
s2 = []

word = list(sys.stdin.readline().strip())
num = int(sys.stdin.readline())
s1 = word

for i in range(num):
    line = sys.stdin.readline().split()

    if line[0]=='L':
        if s1:
            s2.append(s1.pop())
    elif line[0]=='P':
        s1.append(line[1])
    elif line[0]=='D':
        if s2:
            s1.append(s2.pop())
    elif line[0]=='B':
        if s1:
            s1.pop()

s2.reverse()
sys.stdout.write(''.join(s1) + ''.join(s2))