# 백준 온라인 저지 10250번: ACM 호텔
# https://www.acmicpc.net/problem/10250

for _ in range(int(input())):
    h, w, n = map(int, input().split())
    floor = 0
    room = 0
    if n % h == 0:
        floor = h * 100
        room = n // h
    else:
        floor = (n % h) * 100
        room = n // h + 1
    print(floor + room)
