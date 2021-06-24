def solution(n, m):
    answer = [-1, -1]
    
    #gcd
    if m > n:
        m, n = n, m
    a, b = n, m
    r = -1
    
    while(r != 0):
        r = a % b
        a, b = b, r
    answer[0] = a

    #lcm
    answer[1] = (n*m//answer[0])
        
    return answer

print(solution(3, 12))
