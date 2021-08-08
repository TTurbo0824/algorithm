# 백준 온라인 저지 10175번: Dominant Species
# https://www.acmicpc.net/problem/10175

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    location, species = map(str, input().split())
    
    bobcat = species.count("B") * 2
    coyote = species.count("C")
    lion = species.count("M") * 4
    wolf = species.count("W") * 3

    animals = [bobcat, coyote, lion, wolf]

    if animals.count(max(animals)) != 1:
        print("%s: There is no dominant species"%location)
    else:
        animals = {
            bobcat: "Bobcat",
            coyote: "Coyote",
            lion: "Mountain Lion",
            wolf: "Wolf"
        }

        dominant = animals.get(max(animals))
        print("%s: The %s is the dominant species"%(location, dominant))

'''
for _ in range(int(input())):
    a, b=input().split()
    print(a+': ', end='')
    c=[2*b.count('B'), b.count('C'), 4*b.count('M'), 3*b.count('W')]
    d=max(c)
    if c.count(d)>1:
        print('There is no dominant species')
    else:
        print('The '+['Bobcat', 'Coyote', 'Mountain Lion', 'Wolf'][c.index(d)]+' is the dominant species')
'''