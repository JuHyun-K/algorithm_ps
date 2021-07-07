def solution(s):
    leng = len(s)//2
    if(len(s)%2 != 0):
        answer = s[leng]
    else:
        answer = s[leng-1:leng+1]
    return answer



s = "qwer"
print(solution(s))
