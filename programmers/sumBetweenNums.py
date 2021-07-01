def solution(a, b):
    
    if(a == b):
        return a

    if(a > b):
        a, b = b, a
    #두 수를 포함해서 범위를 갖는 list 생성
    betweenList = [num for num in range(a, b+1)]
    answer = sum(betweenList, 0)
    return answer


a,b = 3, 5
print(solution(a,b))
