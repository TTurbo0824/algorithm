# 프로그래머스 연습문제: 자연수 뒤집어 배열로 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12932

# Solution 1

"""
def solution(n):
    answer = []
    arr = list(map(int, str(n)))

    for i in arr:
        answer.insert(0, i)

    return answer
"""

# Solution 2


def solution(n):
    return list(map(int, reversed(str(n))))
