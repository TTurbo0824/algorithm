# 백준 온라인 저지 10177번: Magic Squares
# https://www.acmicpc.net/problem/10177

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)] 
    target = sum(arr[0])
    isMagic = True
    k = 0
    m = 0
    l = 0
    for i in range(n):
        if target != sum(arr[i]):
            isMagic = False
            break   
        m += arr[i][i]
        l += arr[i][-(i+1)]
        if i == n - 1:
            print(m, l)
            if m != target:
                isMagic = False
                break
            elif l != target:
                isMagic = False
                break
        for j in range(n):
            k += arr[j][i]
            if j == n - 1:
                if k != target:
                    isMagic = False
                    break
                k = 0
    
    if isMagic == True:
        print('Magic square of size %d'%n)
    else:
        print('Not a magic square')