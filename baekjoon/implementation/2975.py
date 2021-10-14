# 백준 온라인 저지 2975번: Transactions
# https://www.acmicpc.net/problem/2975

while True:
    n1, t, n2 = map(str, input().split())

    if (n1, t, n2) == ("0", "W", "0"):
        break

    n1 = int(n1)
    n2 = int(n2)

    # Solution 1

    if t == "W":
        if n1 - n2 < -200:
            print("Not allowed")
            continue
        n1 -= n2
    else:
        n1 += n2

    print(n1)

    # Solution 2

    """
    if t == 'W' and n1 - n2 >= -200:
        print(n1 - n2)
    elif t == 'W' and n1 - n2 < -200:
        print('Not allowed')
    elif t == 'D':
        print(n1 + n2)
    """
