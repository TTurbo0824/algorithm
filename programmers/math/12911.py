# 프로그래머스 연습문제: 다음 큰 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12911


def solution(n):
    original = n
    n = format(n, "b")
    one_num = n.count("1")

    i = 0
    answer = "0"

    while True:
        if answer.count("1") == one_num:
            break
        i += 1
        
        answer = format(original + i, "b")

    return int(answer, 2)
