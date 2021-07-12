import sys

n = int(sys.stdin.readline())
cute, notCute = 0, 0
for i in range(n):
    ans = int(sys.stdin.readline())
    if ans:
        cute += 1
    else:
        notCute += 1

print("Junhee is not cute!" if cute < notCute else "Junhee is cute!")
