# 백준 온라인 저지 16316번: Baby Bites
# https://www.acmicpc.net/problem/16316

n = int(input())
m = list(map(str, input().split()))
answer = True

for i in range(n):
    if m[i] != str(i + 1) and m[i] != "mumble":
        answer = False
        print("something is fishy")
        break

if answer == True:
    print("makes sense")
