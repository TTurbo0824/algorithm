# 백준 온라인 저지 10176번: Opposite Words
# https://www.acmicpc.net/problem/10176

for _ in range(int(input())):
    word = input()
    word = word.lower()

    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    answer = False

    for letter in word:
        if letter in alpha:
            if word.count(letter) == word.count(alpha[25 - alpha.index(letter)]):
                answer = True
            else:
                answer = False
                break

    print("No" if answer == False else "Yes")