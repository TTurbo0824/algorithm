# 프로그래머스 월간 코드 챌린지 시즌1: 이진 변환 반복하기
# https://programmers.co.kr/learn/courses/30/lessons/70129


def solution(s):
    zero = 0
    cnt = 0
    s = list(s)

    while True:
        # s가 1이 될 때까지 while문 실행
        if s == ["1"]:
            break

        zero += s.count("0")
        s = ["1"] * s.count("1")
        s = list(format(len(s), "b"))
        cnt += 1

    return [cnt, zero]
