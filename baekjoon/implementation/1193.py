# 백준 온라인 저지 1193번: 분수찾기
# https://www.acmicpc.net/problem/1193

n = int(input())
num = 0
count = 0

for i in range(1, n + 1):
    if num >= n:
        break
    num += i
    count += 1

if count % 2 != 1:
    print(count - (num - n), "/", num - n + 1, sep="")
elif count % 2 == 1:
    print(num - n + 1, "/", count - (num - n), sep="")
