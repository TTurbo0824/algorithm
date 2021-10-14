# 백준 온라인 저지 1978번: 소수 찾기
# https://www.acmicpc.net/problem/1978

a = int(input())

arr = list(map(int, input().split()))


def prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


count = 0

for i in range(a):
    if prime(arr[i]) == True:
        count += 1

print(count)
