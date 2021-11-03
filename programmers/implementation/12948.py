# 프로그래머스 연습문제: 핸드폰 번호 가리기
# https://programmers.co.kr/learn/courses/30/lessons/12948


def solution(phone_number):
    answer = ""
    length = len(phone_number)
    answer = "*" * (length - 4) + phone_number[length - 4 :]
    return answer
