# 백준 온라인 저지 9949번: Hide those Letters
# https://www.acmicpc.net/problem/9949

count = 1

while True:
    a, b = map(str, input().split())

    if (a, b) == ('#', '#'):
        break

    for _ in range(int(input())):
        line = input()
        answer = ''

        if _ == 0 and count == 1:
            print('Case %d' % count)
        elif _ == 0 and count != 1:
            print('\nCase %d' % count)

        for character in line:
            if character.lower() == a or character.lower() == b:
                answer += '_'
            else:
                answer += character
        print(answer)

    count += 1