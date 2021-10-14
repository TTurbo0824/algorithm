# 백준 온라인 저지 16199번: 나이 계산하기
# https://www.acmicpc.net/problem/16199

birth_year, birth_month, birth_day = map(int, input().split())
year, month, day = map(int, input().split())

b = year - birth_year + 1
c = year - birth_year

if month > birth_month:
    a = year - birth_year
elif month == birth_month:
    if day >= birth_day:
        a = year - birth_year
    else:
        a = year - birth_year - 1
else:
    a = year - birth_year - 1

print(a, b, c, sep="\n")
