# 백준 온라인 저지 4375번: 1
# https://www.acmicpc.net/problem/4375

while True:
    try:
        n = int(input())
        ans = "1"
        while True:
            if int(ans) % n == 0:
                print(len(ans))
                break
            ans += "1"

    except EOFError:
        break
