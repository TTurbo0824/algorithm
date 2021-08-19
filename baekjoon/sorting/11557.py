# 백준 온라인 저지 11557번: Yangjojang of The Year
# https://www.acmicpc.net/problem/11557

import sys
input = sys.stdin.readline

# Solution1

for t in range(int(input())):
    ans = [list(map(str, input().split())) for _ in range(int(input()))]
    ans.sort(key=lambda x: -int(x[1]))
    print(ans[0][0])

# Solution 2

'''
for _ in range(int(input())):
    ans = []
    for i in range(int(input())):
        school = list(map(str, input().strip().split()))
        ans.append(school)
    ans.sort(key=lambda x: -int(x[1]))
    print(ans[0][0])
'''
