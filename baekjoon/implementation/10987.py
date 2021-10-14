# 백준 온라인 저지 10987번: 모음의 개수
# https://www.acmicpc.net/problem/10987

vowels = ["a", "e", "i", "o", "u"]
word = list(map(str, input()))
count = 0

for letter in word:
    if letter in vowels:
        count += 1

print(count)
