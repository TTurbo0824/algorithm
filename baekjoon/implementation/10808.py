# 백준 온라인 저지 10808번: 알파벳 개수
# https://www.acmicpc.net/problem/10808

import sys

word = sys.stdin.readline().strip()
alpha = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
arr = [0] * 26

for i in range(26):
    for l in word:
        if alpha[i] in l:
            arr[i] += 1
print(*arr, sep=" ")
