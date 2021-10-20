# 프로그래머스 월간 코드 챌린지 시즌1: 내적
# https://programmers.co.kr/learn/courses/30/lessons/70128

# Solution 1

"""
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer
"""

# Solution 2


def solution(a, b):

    return sum([x * y for x, y in zip(a, b)])
