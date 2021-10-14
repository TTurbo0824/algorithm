# 백준 온라인 저지 4606번: The Seven Percent Solution
# https://www.acmicpc.net/problem/4606

# Solution 1

"""
while True:
    line = input()
    
    if line == '#':
        break
    
    newLine = ''
    for character in line:
        if character == ' ':
            newLine += '%20'
        elif character == '!':
            newLine += '%21'
        elif character == '$':
            newLine += '%24'
        elif character == '%':
            newLine += '%25'
        elif character == '(':
            newLine += '%28'
        elif character == ')':
            newLine += '%29'
        elif character == '*':
            newLine += '%2a'
        else:
            newLine += character
    print(newLine)
"""

# Solution 2

while True:
    line = input()

    if line == "#":
        break

    newLine = ""

    old = [" ", "!", "$", "%", "(", ")", "*"]
    new = ["%20", "%21", "%24", "%25", "%28", "%29", "%2a"]

    for character in line:
        if character in old:
            newLine += new[old.index(character)]
        else:
            newLine += character

    print(newLine)
