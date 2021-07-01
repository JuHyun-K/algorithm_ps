def solution(n):
    answer = n ** 0.5
    answer = str(answer).split('.') #mod 1쓰면...
    
    if(answer[1] == '0'):
        return (int(answer[0])+1)**2
    else:
        return -1


n = 120
print(solution(n))
