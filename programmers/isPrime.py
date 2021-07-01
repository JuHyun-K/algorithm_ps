import math
def solution(n):
    answer = 0 
    tmp = [True for num in range(n+1)]
    now = tmp[answer]
    
    #for i in range(2, int(math.sqrt(n))+1):
    for i in range(2, int(n**0.5)+1):

        if(tmp[i] == True):
            j = 2
            while i*j <= n:
                tmp[i*j] = False
                j += 1
  
    for i in range(2, n+1):
        if tmp[i]:
            answer += 1
    
    return answer


a = 10
print(solution(a))
