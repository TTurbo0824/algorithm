# 백준 온라인 저지 4195번: 친구 네트워크
# https://www.acmicpc.net/problem/4195

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x != y:
        parent[y] = x # x와 y가 서로 다르다면 y의 부모를 x로 설정
        number[x] += number[y] # x 네트워크의 크기 값과 y 네트워크의 크기 값을 더해줌 
        
test = int(input())

for _ in range(test):
    parent = dict()
    number = dict()
    
    num = int(input())
    
    for _ in range(num):
        x, y = input().split(' ')
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        union(x, y)
        print(number[find(x)])