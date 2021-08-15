# 백준 온라인 저지 4949번: 균형잡힌 세상
# https://www.acmicpc.net/problem/4949

import sys

input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '.':
        break
    stack = []
    isBalanced = True

    # 주어진 인풋 문자열 안의 글자를 하나하나 따져보기 전에,
    # '('와 ')'의 개수 혹은 '['와 ']'의 개수가 일치하지 않으면 (=짝을 이루지 않는다면) 우선적으로 균형 잡힌 문자열이 아니라 판단.
    if s.count('(') != s.count(')') or s.count('[') != s.count(']'):
        isBalanced = False
    # 문자열 안에 괄호가 하나도 없는 경우, 자동적으로 균형 잡힌 문자열이라 판단.
    elif s.count('(') == s.count(')') == s.count('[') == s.count(']') == 0:
        isBalanced = True
    else:
        for ch in s:
            # 여는 괄호('(', '[')인지 검사 후, 만약 여는 괄호라면 스택에 넣어준다.
            if ch == '(' or ch == '[':
                stack.append(ch)
            # 닫는 괄호('(', '[')인지 검사 후, 만약 닫는 괄호라면 스택의 원소와 비교하여 균형이 맞는지 검사한다.
            elif ch == ')' or ch == ']':
                # ')'일 경우 '('와 짝을 이루어야 한다.
                if stack and ch == ')'and stack[-1] == '(':
                    stack.pop()
                # ']'일 경우 '['와 짝을 이루어야 한다.
                elif stack and ch == ']' and stack[-1] == '[':
                    stack.pop()
                # 위 사항에 해당되지 않는 모든 경우, 균형이 깨진 것으로 간주한다.
                else:
                    isBalanced = False
                    break

    print('no' if isBalanced == False else 'yes')