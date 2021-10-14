# 백준 온라인 저지 12518번: Centauri Prime (Small2)
# https://www.acmicpc.net/problem/12518

import sys

v = ["a", "e", "i", "o", "u"]

for _ in range(1, int(sys.stdin.readline()) + 1):
    kingdom = sys.stdin.readline().strip()
    if kingdom[-1].lower() == "y":
        print("Case #%d: %s is ruled by %s." % (_, kingdom, "nobody"))
    elif kingdom[-1].lower() in v:
        print("Case #%d: %s is ruled by %s." % (_, kingdom, "a queen"))
    else:
        print("Case #%d: %s is ruled by %s." % (_, kingdom, "a king"))
