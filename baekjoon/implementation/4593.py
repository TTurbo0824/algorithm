# 백준 온라인 저지 4593번: Rock, Paper, Scissors
# https://www.acmicpc.net/problem/4593

while True:
    n = list(map(str, input()))
    m = list(map(str, input()))

    if n and m == ["E"]:
        break

    game = len(n)

    p1 = 0
    p2 = 0

    for i in range(game):
        if n[i] == m[i]:
            p1 += 0
            p2 += 0
        elif (
            (n[i] == "R" and m[i] == "S")
            or (n[i] == "S" and m[i] == "P")
            or (n[i] == "P" and m[i] == "R")
        ):
            p1 += 1
        else:
            p2 += 1

    print("P1: ", p1, "\n", "P2: ", p2, sep="")
