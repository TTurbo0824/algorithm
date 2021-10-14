# 백준 온라인 저지 1543번: 문서 검색
# https://www.acmicpc.net/problem/1543

d = input()
w = input()

index = 0
result = 0

while len(d) - index >= len(w):
    if d[index : index + len(w)] == w:
        result += 1
        index += len(w)
    else:
        index += 1
print(result)
