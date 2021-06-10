# 백준 온라인 저지 6249번: TV Reports
# https://www.acmicpc.net/problem/6249

arr = list(map(int, input().split()))
n = arr[0]
p = arr[1]
h = arr[2]

for _ in range(n):
    dollar = int(input())
    
    if dollar < p:
        print('NTV: Dollar dropped by {} Oshloobs'.format(p - dollar))
    elif h < dollar:
        print('BBTV: Dollar reached {} Oshloobs, A record!'.format(dollar))
        h = dollar
    
    p = dollar    