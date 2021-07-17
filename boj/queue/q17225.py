from sys import stdin

a, b, n = map(int, stdin.readline().split())

sm_orders = list()
js_orders = list()
timestamp = list()
finA = finB = cnt = 0

for _ in range(n):
    time, color, amount = stdin.readline().split()
    time, amount = int(time), int(amount)
    # 포장중에 주문하면 안되므로, finX으로 포장이 완전히 끝난 시간 체크
    # 지수와 성민이가 동시에 포장하려고 하면 안되므로 True, False -> sort()
    if color == 'R': #jisu
        if finB > time:
            time = finB
        for i in range(amount):
            timestamp.append((time + b * i, True))
        finB = time + b * amount
    else: #sungmin
        if finA > time:
            time = finA
        for i in range(amount):
            timestamp.append((time+a*i, False))
        finA = time + a * amount

timestamp.sort(reverse=True)

#포장한 선물 번호
while timestamp:
    top = timestamp.pop()
    if not top[1]:  # sangmin
        cnt += 1
        sm_orders.append(cnt)
    else:  # jisu
        cnt += 1
        js_orders.append(cnt)

print(len(sm_orders))
print(*sm_orders)
print(len(js_orders))
print(*js_orders)
