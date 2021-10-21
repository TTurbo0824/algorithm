# 프로그래머스 연습문제: 정수 제곱근 판별
# https://programmers.co.kr/learn/courses/30/lessons/12934


def solution(n):
    return (n ** 0.5 + 1) ** 2 if n ** 0.5 == int(n ** 0.5) else -1
