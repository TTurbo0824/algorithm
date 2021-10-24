# 프로그래머스 스택/큐: 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586

import math


def solution(progresses, speeds):
    answer = {}

    day = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]

    """
    # 위의 코드를 풀어서 쓴 것
    day = [0 for _ in range(len(progresses))]

    for i in range(len(progresses)):
        day[i] = math.ceil((100 - progresses[i]) / speeds[i])
    """

    for i in range(len(day)):
        # answer의 길이가 0이 아니고 현재 요소가 이전 요소보다 작을 경우
        # 이전의 기능과 현재 기능을 동시에 끝낼 수 있다고 판단
        # answer 마지막 key의 value에 1을 더해준다
        if len(answer) != 0 and (list(answer)[-1] >= day[i]):
            answer[list(answer)[-1]] += 1
        # answer의 길이가 0이거나 현재 요소가 이전 요소보다 클 경우
        # 이전의 기능과 현재 기능을 동시에 끝낼 수 없다고 판단
        # 해당 기능이 완료된 날을 key값으로 가지는 새로운 item을 생성해준다
        # 이때 value는 현시점 이날 완료된 기능의 개수, 즉 1이 된다.
        else:
            answer[day[i]] = 1

    # answer dict에서 value들만 출력
    return list(answer.values())
