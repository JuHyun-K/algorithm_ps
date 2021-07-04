def solution(s, n):
    answer = ''
    #Z -> A, z -> a
    for char in s:
        if(char == ' '):
            answer += ' '
            continue
        
        if(char.islower()) :  #소문자에서
            tmp = (ord(char) - ord('a') + n) % 26 + ord('a')
        elif(char.isupper() and tmp > 90): #대문자
            tmp = (ord(char) - ord('A') + n) % 26 + ord('A')

        answer += chr(tmp)
        
    return answer


s = "a B Z"
n = 1
print(solution(s, n))
