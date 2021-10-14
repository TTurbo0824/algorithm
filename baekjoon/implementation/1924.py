# 백준 온라인 저지 1924번: 2007년
# www.acmicpc.net/problem/1924

x, y = map(int, input().split())

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

day = 0

for i in range(1, x):
    day += months[i - 1]

day += y

print(days[day % 7])
