# 프로그래머스 위클리 챌린지: 8주차_최소직사각형
# https://programmers.co.kr/learn/courses/30/lessons/86491


def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)

    return row * col
