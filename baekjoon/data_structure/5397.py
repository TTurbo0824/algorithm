# 백준 온라인 저지 5397번: 키로거
# https://www.acmicpc.net/problem/5397

n = int(input())

for _ in range(n):
    left = []
    right = []
    cmd = input()
    
    for i in cmd:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    left.extend(reversed(right))
    print(''.join(left))