# 백준 온라인 저지 14909번: 양수 개수 세기
# https://www.acmicpc.net/problem/14909

a = list(map(int, input().split()))
c = 0

for i in a:
    if i > 0:
        c += 1
print(c)
