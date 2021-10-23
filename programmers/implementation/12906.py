# 프로그래머스 연습문제: 같은 숫자는 싫어
# https://programmers.co.kr/learn/courses/30/lessons/12906

# Solution 1

"""
def solution(arr):
    answer = []
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            answer.append(arr[i])
    answer.append(arr[-1])

    return answer
"""

# Solution 2


def solution(arr):
    answer = []
    for i in arr:
        if len(answer) == 0 or answer[-1] != i:
            answer.append(i)
    
    return answer
