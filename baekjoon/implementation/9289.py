# 백준 온라인 저지 9289번: Morse Code
# https://www.acmicpc.net/problem/9289

import sys

for i in range(int(sys.stdin.readline())):
    code = list(map(str, sys.stdin.readline().strip().split()))
    answer = ''
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
    
    for character in code:
        answer += alpha[morse.index(character)]

    print('Case %d: %s' % (i + 1, answer))