# 백준 온라인 저지 12604번: Store Credit (Large)
# https://www.acmicpc.net/problem/12604

import sys

input = sys.stdin.readline

for t in range(1, int(input()) + 1):
    credit = int(input())
    n = int(input())
    items = list(map(int, input().split()))

    x = credit // 2

    if x * 2 == credit and items.count(x) == 2:
        a = items.index(x)
        b = items.index(x, a + 1)
    else:
        md = dict(zip(items, range(n)))

        for a, x in enumerate(items):
            y = credit - x
            if x != y and y in md:
                b = md[y]
                break
    print("Case #%d: %d %d" % (t, a + 1, b + 1))
