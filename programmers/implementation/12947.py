# 프로그래머스 연습문제: 하샤드 수
# https://programmers.co.kr/learn/courses/30/lessons/12947


def solution(x):
    arr = list(str(x))
    temp = 0

    for i in arr: temp += int(i)

    return True if x % temp == 0 else False
