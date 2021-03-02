# 백준 온라인 저지 1758
# https://www.acmicpc.net/problem/1758
import sys

n = int(input())

total_tip = []
count = 0

for _ in range(n):
    total_tip.append(int(sys.stdin.readline().strip()))

total_tip.sort(reverse=True)

for i in range(n):
    tip = total_tip[i] - i
    if tip > 0:
        count += tip
        
print(count)