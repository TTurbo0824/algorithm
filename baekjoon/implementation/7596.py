# 백준 온라인 저지 7596번: MP3 Songs
# https://www.acmicpc.net/problem/7596

import sys

count = 0

while True:
    n = int(sys.stdin.readline())
    
    if n == 0:
        break
    
    songs = []
    
    for _ in range(n):
        song = sys.stdin.readline().rstrip()
        songs.append(song)

    songs.sort()
    count += 1
    
    print(count, *songs, sep="\n")  