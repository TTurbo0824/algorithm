# 백준 온라인 저지 1100번: 하얀 칸
# https://www.acmicpc.net/problem/1100

board = []

for _ in range(8):
    row = list(input())
    board.append(row)
    
cnt = 0

for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0 and board[i][j] == "F":
                cnt += 1
        else:
            if j % 2 == 1 and board[i][j] == "F":
                cnt += 1

print(cnt)