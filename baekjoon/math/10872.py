# 백준 온라인 저지 10872번: 팩토리얼
# https://www.acmicpc.net/problem/10872

# Solution 1

from math import factorial

print(factorial(int(input())))

# Solution 2

'''
def fact(num):
    if num <= 1:
        return 1
    else:
        return num * fact(num - 1)

n = int(input())
print(fact(n))
'''