# 백준 온라인 저지 2609번: 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609

a = list(map(int, input().split()))
a.sort(reverse = False)
n1 = a[0]
n2 = a[1]
x = []
y = 1
num = 0

for i in range(n2):
    num = num + 1
    if n1 % num == 0 and n2 % num ==0:
        x.append(num)

for i in range(1, len(x)):
    while n1 % x[i] == 0 and n2 % x[i] == 0:
        n1 = int(n1 / x[i])
        n2 = int(n2 / x[i])
        y = y * x[i]

print(x[-1], n1 * n2 * y, sep='\n')