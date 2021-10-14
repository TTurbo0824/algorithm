# 프로그래머스 월간 코드 챌린지 시즌3: 없는 숫자 더하기
# https://programmers.co.kr/learn/courses/30/lessons/86051


def solution(numbers):
    answer = sum([1, 2, 3, 4, 5, 6, 7, 8, 9]) - sum(numbers)
    return answer
