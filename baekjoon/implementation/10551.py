# 백준 온라인 저지 10551: STROJOPIS
# https://www.acmicpc.net/problem/10551

import sys

input = sys.stdin.readline

finger = {
    0: ["1", "Q", "A", "Z"],
    1: ["2", "W", "S", "X"],
    2: ["3", "E", "D", "C"],
    3: ["4", "5", "R", "T", "F", "G", "V", "B"],
    4: ["6", "7", "Y", "U", "H", "J", "N", "M"],
    5: ["8", "I", "K", ","],
    6: ["9", "O", "L", "."],
    7: ["0", "-", "=", "P", "[", "]", ";", "'", "/"],
}

ans = [0] * 8
s = input().rstrip()

for ch in s:
    for key, value in finger.items():
        if ch in value:
            ans[key] += 1

print(*ans, sep="\n")
