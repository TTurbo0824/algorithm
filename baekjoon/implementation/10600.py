# 백준 온라인 저지 10600번: Web Colors
# https://www.acmicpc.net/problem/10600

import sys

input = sys.stdin.readline

colors = {
    "White": [255, 255, 255],
    "Silver": [192, 192, 192],
    "Gray": [128, 128, 128],
    "Black": [0, 0, 0],
    "Red": [255, 0, 0],
    "Maroon": [128, 0, 0],
    "Yellow": [255, 255, 0],
    "Olive": [128, 128, 0],
    "Lime": [0, 255, 0],
    "Green": [0, 128, 0],
    "Aqua": [0, 255, 255],
    "Teal": [0, 128, 128],
    "Blue": [0, 0, 255],
    "Navy": [0, 0, 128],
    "Fuchsia": [255, 0, 255],
    "Purple": [128, 0, 128],
}

while True:
    r, g, b = map(int, input().split())

    if r == g == b == -1:
        break

    key = list(colors.keys())
    val = list(colors.values())

    dist = []

    for arr in val:
        dist.append(((arr[0] - r) ** 2 + (arr[1] - g) ** 2 + (arr[2] - b) ** 2) ** 0.5)

    print(key[dist.index(min(dist))])
