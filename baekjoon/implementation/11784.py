# 백준 온라인 저지 11784번: Hex Code
# https://www.acmicpc.net/problem/11784

while True:
    try:
        s = input()
        print(bytearray.fromhex(s).decode())

    except EOFError:
        break