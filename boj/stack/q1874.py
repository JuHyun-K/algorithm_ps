from sys import stdin

n = int(stdin.readline())
stack = []
result = []
flag = False
top = 0

for i in range(1, n+1):
    tmp = int(stdin.readline().rstrip())

    if top < tmp:
        for j in range(top+1, tmp+1):
            stack.append(j)
            result.append('+')

    top = stack[-1] if top < stack[-1] else top

    if stack.pop() != tmp:
        flag = True
    else:
        result.append('-')

if flag:
    print('NO')
else:
    for i in result:
        print(i)

'''
1. top의 역할: 1~n에서 중복되는 숫자가 있으면 안되므로 증가할 idx를 정해줌(idx그자체)
2. 예제2를 보면, 이 문제의 핵심을 알 수 있음
    5/12534에서 34에 주목하면, stack에서 꺼내려는 숫자(tmp)와 pop한 숫자가 다른 순간 실패한 경우임 
3. max와 같이 선형시간이 걸리는 숫자를 쓰면, 시간초과
4. 다음에는 입력값을 한 번에 받는 걸로 해봐야겠음
'''