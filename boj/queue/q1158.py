import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
circle = deque(str(x) for x in range(1, n+1))
result = []
flag = False

while circle:
    if flag:
        result.append(circle.popleft())
        flag = False
    else:
        for _ in range(k-1):
            circle.append(circle.popleft())
        flag = True

print('<', end='')
print(', '.join(result), end='')
print('>')
'''
하나가 빠지기 전까지는 다 뒤에 append
k보다 작으면 그냥 다 popleft() 가 아니라 계속 반복(n이 k보다 작을 때)
n, m = map(int, input().split())
l = list(range(1, n + 1))
r = []
index = 0

while l:
    index = (index + m - 1) % len(l)
    r.append(str(l.pop(index)))

print('<', ', '.join(r), '>', sep='')


'''