from sys import stdin

ans = 0
n, k = map(int, stdin.readline().split())
kinds = list()
for _ in range(n):
    kinds.append(int(stdin.readline().rstrip()))

while k != 0:
    for i in range(len(kinds)-1, -1, -1):
        if (k // kinds[i]) != 0:
            break
    unit = kinds[i]

    ans += k//unit
    k %= unit

print(ans)
# 10~13을 22라인으로..ㅋㅋ
n, k = 10, 4200
while k != 0:
    coin = kinds.pop()
    ans += k//coin
    k %= coin

print(ans)