# 백준 온라인 저지 4504번: 배수 찾기
# https://www.acmicpc.net/problem/4504

n = int(input())

while True:
    a = int(input())
    if a == 0:
        break
    if a % n == 0:
        print(a, " is a multiple of ", n, ".", sep="")
    else:
        print(a, " is NOT a multiple of ", n, ".", sep="")