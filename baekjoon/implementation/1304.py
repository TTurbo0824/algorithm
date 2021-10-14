# 백준 온라인 저지 1304번: Cameras
# https://www.acmicpc.net/problem/13064

import sys

for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()

    if (
        s.find("0") == -1
        and s[0].isdigit()
        and s[0] == s[1]
        and s[2:4].isdigit()
        and s[4].isupper()
        and s[5:8].isdigit()
    ):
        print(s)
