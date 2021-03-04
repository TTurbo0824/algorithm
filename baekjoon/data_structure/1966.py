# 백준 온라인 저지 1966번
# https://www.acmicpc.net/problem/1966

test = int(input())

for _ in range(test):
    n, m = list(map(int, input().split(' ')))
    q = list(map(int, input().split(' ')))
    q = [(i, index) for index, i in enumerate(q)]
    
    count = 0
    
    while True:
        if q[0][0] == max(q, key=lambda x: x[0])[0]:
            count += 1
            if q[0][1] == m:
                print(count)
                break
            else:
                q.pop(0)
        else:
            q.append(q.pop(0))