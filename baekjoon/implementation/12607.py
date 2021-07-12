# 백준 온라인 저지 12607번: T9 Spelling (Small)
# https://www.acmicpc.net/problem/12607

character = {' ': '0', 'a': '2', 'b': '22', 'c': '222', 'd': '3', 'e': '33', 'f': '333', 
             'g': '4', 'h': '44', 'i': '444', 'j': '5', 'k': '55', 'l': '555', 'm': '6', 
             'n': '66', 'o': '666', 'p': '7', 'q': '77', 'r': '777', 's': '7777', 't': '8',
             'u': '88', 'v': '888', 'w': '9', 'x': '99', 'y': '999', 'z': '9999'}

for i in range(int(input())):
    line = input()
    
    ans = ''

    for s in line:
        if ans != '' and ans[-1] == character[s][0]:
            ans += ' ' + character[s]
        else:
            ans += character[s]
            
    print('Case #%d: %s'%(i + 1, ans))