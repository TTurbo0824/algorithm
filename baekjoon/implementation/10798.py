# 백준 온라인 저지 10798번: 세로읽기
# https://www.acmicpc.net/problem/10798

arr = []

for _ in range(5):
    a = input()
    arr.append(a)

for i in range(max(len(w) for w in arr)):
    for j in range(5):
        if i < len(arr[j]):
            print(arr[j][i], end="")
