import sys
v = int(sys.stdin.readline())
votes = sys.stdin.readline().rstrip()
a = votes.count('A')
b = v - a
if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("Tie")
