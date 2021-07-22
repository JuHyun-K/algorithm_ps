from sys import stdin

exp = stdin.readline().rstrip()

stack = []
result = []

for ele in exp:
    if ele == '(':  # 0순위
        stack.append(ele)

    elif ele in ['*', '/']:  # 1순위
        if len(stack) != 0:
            if stack[-1] in ['*', '/']:
                result.append(stack.pop())
        stack.append(ele)

    elif ele in ['+', '-']:  # 2순위
        while len(stack) != 0:
            if stack[-1] in ['*', '/', '+', '-']:
                result.append(stack.pop())
            else:
                break
        stack.append(ele)

    elif ele == ')':
        while True:  # 열린괄호가 나올 때 까지
            p = stack.pop()
            if p == '(':
                break
            result.append(p)
    else:  # 숫자
        result.append(ele)

while stack:
    result.append(stack.pop())

print(''.join(result))
