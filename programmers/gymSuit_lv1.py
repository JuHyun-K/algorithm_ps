def solve(n, lost, reserve):
    answer = 0 #옷을 잃어버렸다가 다시 생긴 학생 수
    
    tmp = [] #임시배열 why? remove하면 원 배열참조에 문제가 생김
    for ele in lost:
        tmp.append(ele)
        
    for los in tmp: #제한사항5) 여벌이 있는 애가 도난 당한 경우부터 
        if(los in reserve):
            reserve.remove(los)
            lost.remove(los)
            answer += 1

    tmp = [] #임시배열2
    for ele in lost:
        tmp.append(ele)
    
    for los in tmp: 
        if(los-1 in reserve): #도난 당한 학생 앞번호가 여벌이 있는지
            reserve.remove(los-1)
            lost.remove(los)
            answer += 1
            continue
        elif(los+1 in reserve):#도난 당한 학생 뒷번호가 여벌이 있는지
            reserve.remove(los+1)
            lost.remove(los)
            answer += 1
            continue
    return answer

def solution(n, lost,reserve):
    a = n - len(lost) #전체학생 수 - 옷이 없는 학생 수 = 옷이 있는 학생수
    a += solve(n, lost, reserve) #옷이있는 학생 수 + 옷이 생긴 학생수 = new옷이 있는 학생수
    return a
