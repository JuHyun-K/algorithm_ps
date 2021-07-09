import sys

n = int(sys.stdin.readline())

flag, winner = False, 0

for i in range(n):
    arr = sorted(list(map(int, sys.stdin.readline().split())))
    # 이전에 한 번 이라도 같은눈3개가 나왔다면
    if flag:
        if len(set(arr)) == 1:
            if winner < arr[0]*1000 + 10000:
                winner = arr[0]*1000 + 10000
        continue

    if len(set(arr)) == 1: #다 같은 수
        flag = True
        if winner < arr[0] * 1000 + 10000:
            winner = arr[0] * 1000 + 10000
    elif len(set(arr)) == 3: #다 다른 수
        if winner < arr[2]*100:
            winner = arr[2]*100
    else:
        if winner < 1000+arr[1]*100:
            winner = 1000+arr[1]*100

print(winner)
