# 백준 온라인 저지 11319번: Count Me In
# https://www.acmicpc.net/problem/11319

v = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

for _ in range(int(input())):
    s = input()
    
    vnum = 0
    cnum = 0

    for ch in s:
        if ch.isalpha():
            if ch in v:
                vnum += 1
            else:
                cnum += 1

    print(cnum, vnum)