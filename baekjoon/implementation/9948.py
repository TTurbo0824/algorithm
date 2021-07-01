# 백준 온라인 저지 9948번: Have you had your birthday yet?
# https://www.acmicpc.net/problem/9948

import sys

input = sys.stdin.readline

while True:
    day, month = map(str, input().strip().split())
    
    months = ["September", "October", "November", "December"]
    
    if day == "0" and month == "#":
        break
    elif day == "4" and month == "August":
        print("Happy birthday")
    elif day == "29" and month == "February":
        print("Unlucky")
    elif (month not in months) or (month == "August" and int(day) < 4):
        print("Yes")
    else:
        print("No")