# 백준 온라인 저지 1874번: 스택 수열
# https://www.acmicpc.net/problem/1874

n = int(input())
stack = []
result = []
count = 0
no_message = True

for _ in range(0, n):
    a = int(input())
    
    while count < a:
        count += 1
        stack.append(count)
        result.append("+")
    
    if stack[-1] == a:
        stack.pop()
        result.append("-")
    else:
        no_message = False
        exit(0)

if no_message == False:
    print("NO")

else:
    print('\n'.join(result))