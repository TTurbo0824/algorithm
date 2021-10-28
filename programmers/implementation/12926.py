# 프로그래머스 연습문제: 시저 암호
# https://programmers.co.kr/learn/courses/30/lessons/12926


def solution(s, n):
    answer = ""
    for i in s:
        if i == " ":
            answer += i
        else:
            if i == i.lower() and ord(i) + n > 122:
                answer += chr(ord(i) + n - 26)
            elif i == i.upper() and ord(i) + n > 90:
                answer += chr(ord(i) + n - 26)
            else:
                answer += chr(ord(i) + n)
    return answer


def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord("A") + n) % 26 + ord("A"))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord("a") + n) % 26 + ord("a"))

    return "".join(s)
