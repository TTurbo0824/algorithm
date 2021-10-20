# 프로그래머스 연습문제: 두 정수 사이의 합
# https://programmers.co.kr/learn/courses/30/lessons/12912

# Solution 1

"""
def solution(a, b):
    answer = 0
    if a > b:
        a, b = b, a

    for i in range(a, b + 1):
        answer += i

    return answer
"""

# Solution 2


def solution(a, b):
    if a > b:
        a, b = b, a

    return sum(range(a, b + 1))
