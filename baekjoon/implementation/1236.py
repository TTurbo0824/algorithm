# 백준 온라인 저지 1236번: 성 지키기
# https://www.acmicpc.net/problem/1236

n, m = map(int, input().split())
array = []

for _ in range(n):
    array.append(input())

row_count, col_count = 0, 0

for i in range(n):
    if "X" not in array[i]:
        row_count += 1

for j in range(m):
    if "X" not in [array[i][j] for i in range(n)]:
        col_count += 1
print(max(row_count, col_count))
