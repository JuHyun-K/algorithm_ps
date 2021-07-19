import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
ans = 0
names = deque(deque() for _ in range(19))

for rank in range(n):
    length = len(input().rstrip()) - 2

    while names[length]:
        base = names[length][0]
        if rank - base <= k:
            ans += len(names[length])
            break
        else:
            names[length].popleft()
    names[length].append(rank)

print(ans)

# sliding window
'''
https://www.acmicpc.net/source/25578577
from _collections import deque

input = __import__('sys').stdin.readline
n, k = map(int,input().split())
l = [len(input()) for i in range(n)]
ans = 0
dic = {}
Q = deque([])
for i in range(n):
    key = l[i]
    if key in dic:
        ans+=dic[key]  # 한쌍이니까 더하고 추가
        dic[key]+=1
    else:
        dic[key]=1
    Q.append(key)
    # sliding window
    if k <= i:  # k등 밖이니까 볼 필요 없으므로 -1(만약 k 안이였으면 건들ㄴ)
        j = Q.popleft()
        dic[j] -= 1

print(ans)
'''


'''
for rank in range(n):
    name = queue[이름길이]의 내용물과 비교
    
    base = q[leng][0] # 맨처음 것
    while q[leng]:
        if rank - base <= k: #범위 내이면 
            ans += len(q[leng])
            break
        else: # 범위 밖이면 pop
            q[leng].popleft()
    
    names[leng].append(rank)
'''