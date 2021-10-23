# 프로그래머스 연습문제: 문자열 다루기 기본
# https://programmers.co.kr/learn/courses/30/lessons/12918


def solution(s):
    return True if s.isnumeric() == True and (len(s) == 4 or len(s) == 6) else False
