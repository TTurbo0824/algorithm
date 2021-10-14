# 백준 온라인 저지 12603번: Store Credit (Small)
# https://www.acmicpc.net/problem/12603

import sys

input = sys.stdin.readline

for t in range(1, int(input()) + 1):
    credit = int(input())
    n = int(input())
    items = list(map(int, input().split()))
    ans = []

    for i in range(n):
        for j in range(1, n):
            if items[i] + items[j] == credit and i != j:
                ans.append(i)
                ans.append(j)

    print("Case #%d: %d %d" % (t, ans[0] + 1, ans[1] + 1))
