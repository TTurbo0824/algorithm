# 백준 온라인 저지 4072번: Words
# https://www.acmicpc.net/problem/4072

while True:
    line = input()
    
    if line == "#":
        break
        
    arr = line.split(" ")

    for el in arr:
        print(el[::-1], end=" ")