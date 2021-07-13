# 백준 온라인 저지 10181번: Federation Favorites
# https://www.acmicpc.net/problem/10181

while True:
    n = int(input())

    if n == -1:
        break

    divisor = []

    for d in range(1, n):
        if n % d == 0:
            divisor.append(d)
            
    if n == sum(divisor):
        print(f'{n} = ' + ' + '.join(map(str, divisor)))
    else:
        print(f'{n} is NOT perfect.')