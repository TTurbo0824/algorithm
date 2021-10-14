# 백준 온라인 저지 2309번: 일곱 난쟁이
# https://www.acmicpc.net/problem/2309

n = 9
arr = []

for i in range(n):
    a = int(input())
    arr.append(a)

target = sum(arr) - 100
one = 0
two = 0

for i in range(n):
    for j in range(1, n):
        if arr[i] + arr[j] == target:
            one = arr[i]
            two = arr[j]

arr.remove(one)
arr.remove(two)
arr.sort()

for i in arr:
    print(i)
