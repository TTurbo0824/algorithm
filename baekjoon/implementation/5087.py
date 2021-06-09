# 백준 온라인 저지 5087번: Card Cutting
# https://www.acmicpc.net/problem/5087

while True:
    k = input()
    
    if k == "#":
        break

    cards = list(map(str, k.split()))
    cards.pop()
    
    cscore = 0
    tscore = 0

    for card in cards:
        if card == 'A':
            card = 1
        
        if int(card) % 2 == 1:
            cscore += 1
        else:
            tscore += 1

    if cscore > tscore:
        print("Cheryl")
    elif cscore < tscore:
        print("Tania")
    else:
        print("Draw")