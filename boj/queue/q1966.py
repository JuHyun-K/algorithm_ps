from sys import stdin
from collections import deque

tc = int(stdin.readline())
result = list()

for _ in range(tc):
    n, m = map(int, stdin.readline().split())
    priority = list(map(int, stdin.readline().split()))
    q = deque()  # 큐에 우선순위값과 boolean값을 저장(내가 보고자하는건 true, 나머지는 false)
    idx = 0

    # 입력
    for i in range(n):
        if i == m:
            q.append((priority[i], True))
        else:
            q.append((priority[i], False))
    priority.sort()  #  우선순위 큐 정렬 -> max값이 항상 맨 뒤

    # 처리
    while True:
        out = q.popleft()  # 큐의 처음 값을 가져옴
        if out[0] != priority[-1]:  # 큐 값과 max값이 다르면, 다시 큐의 맨뒤로
            q.append(out)
        else:  # 같으면, 우선순위 큐에서도 삭제, 출력+1
            priority.pop()
            idx += 1
            if out[1]:  # 출력된 값이 내가 찾는 값이면(true) 다음 tc로
                break
    result.append(idx)

for ele in result:
    print(ele)
