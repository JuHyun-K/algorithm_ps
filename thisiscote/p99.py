from sys import stdin

n, k = map(int, stdin.readline().split())
n1 = n
cnt = 0
while n >= k or n != 1:
    if n%k == 0:
        n //= k
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)

result = 0
n, k = 25, 3
while True:
    target = (n//k) * k
    result += (n-target)
    n = target

    if n < k:
        break
    result += 1
    n //= k

result += (n-1)
print(result)