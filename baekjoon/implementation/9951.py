# 백준 온라인 저지 9951번: Word Extraction
# https://www.acmicpc.net/problem/9951

import sys

input = sys.stdin.readline

count = 0

while True:
    s = input().strip()
    if s == "#":
        break
    
    s = s.lower()
    temp = ''
    
    for ch in s:
        if ch.isalpha() or ch.isnumeric() or ch == " ":
            temp += ch

    temp = sorted(temp.split(" "))
    result = []

    for word in temp:
        if word not in result and word != '' and word.isnumeric() == False:
            result.append(word)

    if count != 0:
        print()
    print(*result, sep="\n")

    count += 1