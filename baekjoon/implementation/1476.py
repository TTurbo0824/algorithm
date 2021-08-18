# 백준 온라인 저지 1476번: 날짜 계산
# https://www.acmicpc.net/problem/1476

E, S, M, year = 1, 1, 1, 1

ET, ST, MT = map(int, input().split())

while True:
    if ET == E and ST == S and MT == M:
        break
        
    E += 1
    S += 1
    M += 1
    year += 1
    
    if E >= 16:
        E -= 15
    if S >= 29:
        S -= 28
    if M >= 20:
        M -= 19

print(year)