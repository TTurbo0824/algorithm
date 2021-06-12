# 백준 온라인 저지 4841번: Look and Say
# https://www.acmicpc.net/problem/4841

import sys

for _ in range(int(sys.stdin.readline())):
    line = sys.stdin.readline().strip()
    arr = [[0, 0]]
    answer = ''

    for num in line:
        n = 1
        if arr[-1][1] != num:
            arr.append([n, num]) 
        else:
            arr[-1][0] += 1
            
    arr = arr[1:len(arr)]
    
    for i in arr:
        for j in i:
            answer += str(j)

    print(answer)