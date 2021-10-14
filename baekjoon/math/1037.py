# 백준 온라인 저지 1037번: 약수
# https://www.acmicpc.net/problem/1037

n = int(input())
a = list(map(int, input().split()))

a_max = max(a)
a_min = min(a)

print(a_max * a_min)
