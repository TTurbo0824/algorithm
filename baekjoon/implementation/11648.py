# 백준 온라인 저지 11648번: 지속
# https://www.acmicpc.net/problem/11648

from functools import reduce

n = input()
arr = list(n)

count = 0
while len(arr) > 1:
    n = reduce(lambda x, y: int(x) * int(y), arr)
    arr = list(str(n))
    print(arr)
    count += 1
print(count)