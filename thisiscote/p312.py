from sys import stdin

s = list(map(int, stdin.readline().rstrip()))
print(s)
ans = s[0]
tmp = ''

for i in range(1, len(s)):
    x = s[i]
    # if tmp:
    #     a = eval(tmp+str(x))
    #     ans += a
    #     tmp = ''
    #     continue

    if x <= 1 or ans <= 1:  # ans <= 1...haha..
        ans += x
    else:
        ans *= x

print(ans)
