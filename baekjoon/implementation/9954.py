# 백준 온라인 저지 9954번: Cedric's Cypher
# https://www.acmicpc.net/problem/9954

while True:
    s = input()

    if s == '#':
        break

    shift = ord(s[-1]) - ord('A')
    s = s[0:len(s)-1]
    answer = ''

    for ch in s:
        if ord('A') <= ord(ch) <= ord('Z'):
            if ord(ch) - shift < ord('A'):
                answer += chr(ord('Z') - (shift - (ord(ch) - ord('A')) - 1))
            else:
                answer += chr(ord(ch) - shift)
        elif ord('a') <= ord(ch) <= ord('z'):
            if ord(ch) - shift < ord('a'):
                answer += chr(ord('z') - (shift - (ord(ch) - ord('a')) - 1))
            else:
                answer += chr(ord(ch) - shift)
        else:
            answer += ch

    print(answer)