# 백준 온라인 저지 2908번: 상수
# https://www.acmicpc.net/problem/2908

a, b = input().split()

def reverse_num(num):
    arr = []
    for i in range(len(num)):
        arr.append(num[len(num)-i-1])
    return int("".join(arr))

new_a = reverse_num(a)
new_b = reverse_num(b)

if new_a > new_b:
    print(new_a)
else:
    print(new_b)