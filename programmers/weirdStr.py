def solution(s):
    answer = []
    #한글자씩 대소문자로 바꾸고 -> tmp에 접착 -> join사용
    
    s = s.upper()
    s = s.split(' ')
    s = list(map(list, s))
    
    for x in s:
        tmp = ''
        for i in range(0, len(x)):
            if(i%2 == 0):
                c = x[i].upper() #list 원소에서 작업하는 것이 아니
            else:
                c = x[i].lower()
            tmp += c
        answer.append(tmp)
    return ' '.join(answer)
        

s = "try hello world"
print(solution(s))
