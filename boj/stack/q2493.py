from sys import stdin

n = int(stdin.readline())
towers = list(map(int, stdin.readline().split()))
result = []
stack = []  # 튜플 넣는 스택(위치, 타워값)
result = []

for i in range(len(towers)):

    while stack:
        if stack[-1][1] > towers[i]: # 수신 성공
            result.append(stack[-1][0]+1)
            break
        else:
            stack.pop()

    if not stack:
        result.append(0)
    stack.append((i, towers[i]))  # 더 가까운 타워를 수신받아야하므로

print(*result)

print("-------------------------------------------------------------")

n = int(stdin.readline())
towers = list(map(int, stdin.readline().split()))
result = [0]*n

for i in range(1, n):
    idx = i-1
    while True:
        if towers[i] <= towers[idx]:  # 수신성공
            result[i] = idx+1
            break
        else:  # 수신 실패
            idx = result[idx]-1  # 그 앞자리를 확인 -> 0이 아니면 다시 확인
            if idx == -1:  #  그  앞자리도 0이면 -> 아예 다음 것을 비교
                break
print(*result)
