def solution(s):
    p_count = 0
    y_count = 0

    s = s.lower() #다 소문자로

    p_count = s.count('p')
    y_count = s.count('y')

    return True if(p_count == y_count) else False

    
    
    
    



s = "pPoooyY"
print(solution(s))
