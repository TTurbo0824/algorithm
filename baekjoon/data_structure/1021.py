# 백준 온라인 저지 1021번: 회전하는 큐
# https://www.acmicpc.net/problem/1021

n, m = map(int, input().split())
s = list(map(int, input().split()))
q = [i for i in range(1, n + 1)]
count = 0

for i in range(m):
    q_len = len(q)
    q_index = q.index(s[i])
    if q_index < q_len - q_index: # 해당 q가 앞쪽에 가까운지, 아니면 뒷쪽에 가까운지 판단
        while True:
            if q[0] == s[i]:
                del q[0]
                break
            else:
                q.append(q[0])
                del q[0]
                count += 1
    else:
        while True:
            if q[0] == s[i]:
                del q[0]
                break
            else:
                q.insert(0, q[-1])
                del q[-1]
                count += 1

print(count)