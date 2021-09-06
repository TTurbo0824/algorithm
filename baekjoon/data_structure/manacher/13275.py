# 백준 온라인 저지 13275번: 가장 긴 팰린드롬 부분 문자열
# https://www.acmicpc.net/problem/13275

s = "#" + "#".join(list(input())) + "#"

n, r, k = len(s), -1, -1
p = [0] * n

for i in range(n):
    if i <= r:
        p[i] = min(r - i, p[2 * k - i])

    while i - p[i] >= 1 and i + p[i] < n - 1 and s[i - p[i] - 1] == s[i + p[i] + 1]:
        p[i] += 1

    if r < i + p[i]:
        r = i + p[i]
        k = i

print(max(p))