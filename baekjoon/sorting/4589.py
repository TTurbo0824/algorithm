# 백준 온라인 저지 4589번: Gnome Sequencing
# https://www.acmicpc.net/problem/4589

n = int(input())
print("Gnomes:")

for _ in range(n):
    gnomes = list(map(int, input().split()))
    if gnomes == sorted(gnomes) or gnomes == sorted(gnomes, key = lambda x : -x):
        print("Ordered")
    else:
        print("Unordered")