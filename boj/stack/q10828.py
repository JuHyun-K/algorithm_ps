from sys import stdin

n = int(stdin.readline())
stack = list()

for _ in range(n):
    order = list(stdin.readline().rstrip().split())

    if order[0] == 'push':
        stack.append(int(order[1]))
    elif order[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    else:  # top
        if stack:
            print(stack[-1])
        else:
            print(-1)
