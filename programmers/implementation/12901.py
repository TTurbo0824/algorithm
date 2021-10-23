# 프로그래머스 연습문제: 2016년
# https://programmers.co.kr/learn/courses/30/lessons/12901

# Solution 1

import pandas as pd


def solution(a, b):
    answer = ""
    date = "2016-%d-%d" % (a, b)
    temp = pd.Timestamp(date)
    answer = temp.day_name()[0:3]

    return answer.upper()


# Solution 2

"""
def solution1(a, b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

    return days[(sum(months[: a - 1]) + b - 1) % 7]
"""
