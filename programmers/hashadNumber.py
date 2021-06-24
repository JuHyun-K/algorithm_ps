def solution(x):
    answer = True
    digitSum = sum(map(int, str(x)))

    if(x % digitSum == 0):
        return answer
    else:
        return False



for i in range(10, 14):
    print(i, solution(i))
