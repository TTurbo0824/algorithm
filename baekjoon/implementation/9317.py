# 백준 온라인 저지 9317번: Monitor DPI
# https://www.acmicpc.net/problem/9317

import sys
input = sys.stdin.readline

while True:
    d, wp, hp = map(float, input().split())

    if d == wp == hp == 0.0:
        break

    w = 16 * d / (337 ** 0.5)
    h = 9 / 16 * w
    wr = wp / w
    hr = hp / h

    print("Horizontal DPI: %0.2f" % (wr))
    print("Vertical DPI: %0.2f" % (hr))