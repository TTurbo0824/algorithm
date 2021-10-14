# 백준 온라인 저지 1668번: 트로피 진열
# https://www.acmicpc.net/problem/1668


def ascending(array):
    now = array[0]
    count = 1
    for i in range(1, len(array)):
        if now < array[i]:
            count += 1
            now = array[i]
    return count


n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

print(ascending(arr))
arr.reverse()
print(ascending(arr))
