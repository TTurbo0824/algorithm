# 백준 온라인 저지 17427번: 약수의 합 2
# https://www.acmicpc.net/problem/17427

n = int(input())

answer = 0

for i in range(1, n + 1):
    # i의 배수의 개수 = i를 약수로 갖는 수
    answer += (n // i) * i

print(answer)