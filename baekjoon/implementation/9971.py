# 백준 온라인 저지 9971번: The Hardest Problem Ever
# https://www.acmicpc.net/problem/9971

character = {'A': 'V', 'B': 'W', 'C': 'X', 'D': 'Y', 'E': 'Z', 'F': 'A', 'G': 'B',
             'H': 'C', 'I': 'D', 'J': 'E', 'K': 'F', 'L': 'G', 'M': 'H', 'N': 'I',
             'O': 'J', 'P': 'K', 'Q': 'L', 'R': 'M', 'S': 'N', 'T': 'O', 'U': 'P',
             'V': 'Q', 'W': 'R', 'X': 'S', 'Y': 'T', 'Z': 'U'}

while True:
    component_1 = input()

    if component_1 == 'ENDOFINPUT':
        break

    print(
        ''.join(map(lambda s: character[s] if s in character else s, input())))

    component_2 = input()
