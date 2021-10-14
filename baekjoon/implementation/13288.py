# 백준 온라인 저지 13288번: A New Alphabet
# https://www.acmicpc.net/problem/13288

# Solution 1

alpha = [
    " ",
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
symbol = [
    " ",
    "@",
    "8",
    "(",
    "|)",
    "3",
    "#",
    "6",
    "[-]",
    "|",
    "_|",
    "|<",
    "1",
    "[]\/[]",
    "[]\[]",
    "0",
    "|D",
    "(,)",
    "|Z",
    "$",
    "']['",
    "|_|",
    "\/",
    "\/\/",
    "}{",
    "`/",
    "2",
]

s = input().lower()

answer = ""

for character in s:
    if character in alpha:
        answer += symbol[alpha.index(character)]
    else:
        answer += character

print(answer)

# Solution 2

"""
character = {'a': '@', 'b': '8', 'c': '(', 'd': '|)', 'e': '3', 'f': '#', 'g': '6',
      'h': '[-]', 'i': '|', 'j': '_|', 'k': '|<', 'l': '1', 'm': '[]\\/[]',
      'n': '[]\\[]', 'o': '0', 'p': '|D', 'q': '(,)', 'r': '|Z', 's': '$',
      't': "']['", 'u': '|_|', 'v': '\\/', 'w': '\\/\\/', 'x': '}{',
      'y': '`/', 'z': '2'}

print(''.join(map(lambda s: character[s] if s in character else s, input().lower())))
"""
