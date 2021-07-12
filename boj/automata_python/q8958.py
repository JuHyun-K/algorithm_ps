import sys

n = int(sys.stdin.readline())

for i in range(n):
    score, tmp = 0, 0
    s = sys.stdin.readline().rstrip()
    for j in range(len(s)):
        if s[j] == 'O':
            score = score + tmp + 1
            tmp += 1
        else:
            tmp = 0
    print(score)