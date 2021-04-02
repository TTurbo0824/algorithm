# 백준 온라인 저지 2292번: 벌집
# https://www.acmicpc.net/problem/2292

n = int(input())
pile = 1
count = 1
arr = []

while n > pile:
    pile += count * 6
    count += 1

print(count)