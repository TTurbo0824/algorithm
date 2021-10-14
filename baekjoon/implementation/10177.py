# 백준 온라인 저지 10177번: Magic Squares
# https://www.acmicpc.net/problem/10177

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    target = sum(arr[0])  # 타겟 설정
    col = 0  # 세로 비교 변수
    leftDiagonal = 0  # 좌측 대각선 비교 변수
    rightDiagonal = 0  # 우측 대각선 비교 변수
    isMagic = True  # Magic square 여부 판단

    for i in range(n):
        # 가로줄 검사
        if target != sum(arr[i]):
            isMagic = False
            break
        leftDiagonal += arr[i][i]
        rightDiagonal += arr[i][-(i + 1)]

        if i == n - 1:
            # 좌측 대각선 검사
            if leftDiagonal != target:
                isMagic = False
                break
            # 우측 대각선 검사
            elif rightDiagonal != target:
                isMagic = False
                break
        # 세로줄 검사
        for j in range(n):
            col += arr[j][i]
            if j == n - 1:
                if col != target:
                    isMagic = False
                    break
                col = 0
    print("Magic square of size %d" % n if isMagic == True else "Not a magic square")
