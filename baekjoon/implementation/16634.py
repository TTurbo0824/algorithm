# 백준 온라인 저지 16634번: Run-Length Encoding, Run!
# https://www.acmicpc.net/problem/16634

import sys

input = sys.stdin.readline

c, s = input().strip().split()

# Solution 1


def e(line):
    arr = [[0, 0]]
    answer = ""

    for num in line:
        n = 1
        if arr[-1][0] != num:
            arr.append([num, n])
        else:
            arr[-1][1] += 1
    arr = arr[1 : len(arr)]

    for i in arr:
        for j in i:
            answer += str(j)
    return answer


def d(line):
    answer = ""
    for i in range(len(line)):
        if i % 2 == 0:
            answer += line[i] * int(line[i + 1])
    return answer


if c == "E":
    print(e(s))
elif c == "D":
    print(d(s))

# Solution 2

"""

if c == 'E':
    base = None
    k = 0
    answer = ''
    for i in s:
        if base == None:
            base = i
            k += 1
        else:
            if i == base: k += 1
            else:
                answer += base
                answer += str(k)
                base = i
                k = 1
    answer += base
    answer += str(k)
    print(answer)
else:
    answer = ''
    for i in range(len(s)//2):
        v, k = s[i*2:i*2+2]
        answer += v*int(k)
    print(answer)
"""
