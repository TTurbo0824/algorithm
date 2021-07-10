# 백준 온라인 저지 13224번: Chop Cup
# https://www.acmicpc.net/problem/13224

moves = input()

ball = [1, 0, 0]

for m in moves:
    if m == 'A':
        tempL = ball[0]
        tempM = ball[1]
        ball[0] = tempM
        ball[1] = tempL
    elif m == 'B':
        tempM = ball[1]
        tempR = ball[2]
        ball[1] = tempR
        ball[2] = tempM
    elif m == 'C':
        tempL = ball[0]
        tempR = ball[2]
        ball[0] = tempR
        ball[2] = tempL

print(ball.index(1) + 1)