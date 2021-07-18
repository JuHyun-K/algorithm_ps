from sys import stdin
from collections import deque

n = int(stdin.readline())
q = deque()

for _ in range(n):
    order = list(stdin.readline().rstrip().split())

    if order[0] == 'push':
        q.append(order[1])
    elif order[0] == 'pop':
        print(q.popleft()) if q else print(-1)
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        print(0) if q else print(1)
    elif order[0] == 'front':
        print(q[0]) if q else print(-1)
    else:
        print(q[-1]) if q else print(-1)
