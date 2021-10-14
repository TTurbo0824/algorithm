# 백준 온라인 저지 4581번: Voting
# https://www.acmicpc.net/problem/4581

while True:
    votes = input()

    if votes == "#":
        break

    total = len(votes)
    yes = votes.count("Y")
    no = votes.count("N")
    absent = votes.count("A")

    if absent >= total / 2:
        print("need quorum")
    elif yes > no:
        print("yes")
    elif no > yes:
        print("no")
    elif yes == no:
        print("tie")
