# 백준 온라인 저지 18512번: 점프 점프
# https://www.acmicpc.net/problem/18512

x, y, p1, p2 = map(int, input().split())

x_path = [p1]
y_path = [p2]
answer = -1
count = 1

while True:
    p1 += x
    p2 += y
    x_path.append(p1)
    y_path.append(p2)

    if p1 in y_path or p2 in x_path:
        answer = min(p1, p2)
        break
    elif count > 1000:
        break
    count += 1

print(answer)
