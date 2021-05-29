# 백준 온라인 저지 2920번: 음계
# https://www.acmicpc.net/problem/2920

'''
# Solution 1

n = list(map(int, input().split(' ')))
asc = sorted(n)
des = sorted(n, reverse=True)

if n == asc:
    print("ascending")
elif n == des:
    print("descending")
else: print("mixed")
'''

# Solution 2

# map을 이용해 각각의 원소를 int형으로 바꿔준다
n = list(map(int, input().split(' ')))

ascending = True
descending = True

# 두 번째 원소부터 앞의 원소와 비교 시작
for i in range(1, 8):
    if n[i] > n[i - 1]:
        descending = False
    elif n[i] < n[i - 1]:
        ascending = False
        
if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")