# 백준 온라인 저지 1157번: 단어 공부
# https://www.acmicpc.net/problem/1157

a = input().upper()
word = list(set(a))
new = []

for i in word:
    count = a.count(i)
    new.append(count)

if new.count(max(new)) >= 2:
    print("?")
else:
    print(word[new.index(max(new))])
