# 백준 온라인 저지 13234번: George Boole
# https://www.acmicpc.net/problem/13234

v1, op, v2 = map(str, input().split())

if op == "AND":
    if v1 == v2:
        print(v1)
    else:
        print("false")
elif op == "OR":
    if v1 == v2:
        print(v1)
    else:
        print("true")