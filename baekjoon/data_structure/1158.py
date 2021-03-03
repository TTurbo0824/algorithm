# 백준 온라인 저지 1158번
# https://www.acmicpc.net/problem/1158

n, k = map(int,input().split())
arr = [i for i in range(1, n + 1)]
num = 0
answer = []

for i in range(n):
    num += k - 1
    
    if num >= len(arr):
        num = num % (len(arr))

    answer.append(arr.pop(num))
    
print("<", ', '.join(str(e) for e in answer),">", sep='')