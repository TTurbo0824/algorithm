# 백준 온라인 저지 2920번
# https://www.acmicpc.net/problem/2920

n = list(map(int, input().split()))
asc = sorted(n)
des = sorted(n, reverse=True)

if n == asc:
    print("ascending")
elif n == des:
    print("descending")
else: print("mixed")