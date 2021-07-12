import sys

n = int(sys.stdin.readline())
c_score, s_score = 100, 100

for i in range(n):
    c, s = map(int, sys.stdin.readline().split())
    if c == s:
        continue

    if c > s:
        s_score -= c
    else:
        c_score -= s

print(c_score)
print(s_score)