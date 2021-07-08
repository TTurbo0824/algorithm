# 백준 온라인 저지 13775번: Virus
# https://www.acmicpc.net/problem/13775

n = int(input())
s = input()

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ans = ''
k = 0

for i in range(len(s)):
    if s[i].isalpha():
        if n + k > 25:
            n = (n + k) % 25 - k
        dec = alpha.index(s[i]) - (n + k)
        if dec < 0:
            dec += 26
        ans += alpha[dec]
        k += 1
    else:
        ans += s[i]

print(ans)