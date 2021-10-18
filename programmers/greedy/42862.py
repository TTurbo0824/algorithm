# 프로그래머스 탐욕법(Greedy): 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862


def solution(n, lost, reserve):
    answer = 0
    lost_num = len(lost)
    lost.sort()
    reserve.sort()
    lost_copy = lost.copy()
    reserve_copy = reserve.copy()

    # 제공자가 여별의 체육복 도둑맞음
    for i in lost_copy:
        if i in reserve_copy:
            reserve.remove(i)
            lost.remove(i)
            lost_num -= 1

    for i in lost:
        # 바로 앞 학생 체육복을 빌림
        if i - 1 in reserve:
            reserve.remove(i - 1)
            lost_num -= 1
        # 바로 뒤 학생 체육복을 빌림
        elif i + 1 in reserve:
            reserve.remove(i + 1)
            lost_num -= 1

    answer = n - lost_num
    return answer
