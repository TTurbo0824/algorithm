# 백준 온라인 저지 2869번: 달팽이는 올라가고 싶다 
# https://www.acmicpc.net/problem/2869

a, b, v = map(int, input().split())
day = 0

if (v - b) % (a - b) != 0:
    day = ((v - b) // (a - b)) + 1
else:
    day = ((v - b) // (a - b))
    
print(day)