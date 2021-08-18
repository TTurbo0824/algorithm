# 백준 온라인 저지 10430번: 나머지
# https://www.acmicpc.net/problem/10430

A, B, C = map(int, input().split())

# Solution 1
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

# Solution 2
'''
print(eval('(A+B)%C'))
print(eval('((A%C) + (B%C))%C'))
print(eval('(A*B)%C'))
print(eval('((A%C)*(B%C))%C'))
'''