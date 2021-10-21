# 프로그래머스 완전탐색: 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840


def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    first = first * (len(answers) // len(first) + 1)
    second = second * (len(answers) // len(second) + 1)
    third = third * (len(answers) // len(third) + 1)

    total = [0, 0, 0]

    for i in range(0, len(answers)):
        if answers[i] == first[i]:
            total[0] += 1
        if answers[i] == second[i]:
            total[1] += 1
        if answers[i] == third[i]:
            total[2] += 1

    for i in range(0, 3):
        if max(total) == total[i]:
            answer.append(i + 1)

    return answer
