def solution(n):
    answer = 0


    for x in range(1, n+1):
        if(x*x > n): #약수, 소수 등을 구할 때 n의 루트보다 큰 수는 볼 필요x
            break

        if(n % x == 0):
            answer += x
            if(n//x != x): #5*5=25와 같은 경우 제외(제곱수)
                answer += n//x
            
    return answer


n = 25
print(solution(n))
