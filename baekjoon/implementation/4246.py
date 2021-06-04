# 백준 온라인 저지 4246번: To and Fro
# https://www.acmicpc.net/problem/4246

import sys

# Solution 1
while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    line = sys.stdin.readline().strip()
    arr = []
    
    for i in range(len(line) // n):
        if not i % 2:
            arr.append(line[i * n:i * n + n])
        else:
            arr.append(line[i * n:i * n + n][::-1])

    print(*map(lambda x: ''.join(x), zip(*arr)), sep='')


# Solution 2

'''
while True:
    n = int(sys.stdin.readline())
    
    if n == 0:
        break
        
    line = sys.stdin.readline().strip()
    arr = []
    answer = ""
    counter = 0
    
    for i in range(0, len(line), n):
        counter += 1
        if (counter %2 == 1):
            arr.append(line[i:i + n])
        else:
            arr.append(line[i:i + n][::-1])

    for k in range(len(arr[0])):
        for j in range(len(arr)):
            if k < len(arr[j]):
                answer += arr[j][k]
    print(answer)
'''