# 백준 온라인 저지 4287번: Word Ratios
# https://www.acmicpc.net/problem/4287

while True:
    k = input()

    if k == "#":
        break

    words = list(k.split())
    first, second, third = words
    fourth = ""
    alpha = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    for i in range(len(first)):
        n = alpha.index(first[i]) - alpha.index(second[i])

        if alpha.index(third[i]) - n > len(alpha) - 1:
            fourth += alpha[alpha.index(third[i]) - n - len(alpha)]
        else:
            fourth += alpha[alpha.index(third[i]) - n]

    words.append(fourth)
    print(" ".join(words))
