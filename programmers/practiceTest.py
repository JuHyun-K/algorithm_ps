def solution(answers):
    #수포자 패턴->규칙을 너무 찾을려하지말
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5] 
    num3 = [3,3,1,1,2,2,4,4,5,5]
    scores = [0, 0, 0] #점수기록
    i=0 

    for ans in answers:
        #num1
        if(ans == num1[i%5]):
            scores[0] += 1
        #num2
        if(ans == num2[i%8]):
            scores[1] += 1
        #num3
        if(ans == num3[i%10]):
            scores[2] += 1
        i += 1
        
    maxV = max(scores) #최고점
    res_list = [j+1 for j, value in enumerate(scores) if value == maxV] #최고점과 같은 학생이 있나
    return res_list