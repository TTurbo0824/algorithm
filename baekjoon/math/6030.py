# 백준 온라인 저지 6030번: Scavenger Hunt 
# https://www.acmicpc.net/problem/6030

p, q = map(int, input().split())

def get_factors(num):
    factors = []
    
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

pfactors = get_factors(p)
qfactors = get_factors(q)      

for i in pfactors:
    for j in qfactors:
        print(i, j)