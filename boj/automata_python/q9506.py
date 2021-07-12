while True:
    n = int(input())
    if n == -1: break

    factor = [1]
    for i in range(2, n):
        if i*i >= n: break
        if n % i == 0:
            factor.append(i)
            factor.append(n//i)
    factor.sort()
    summ = sum(factor)

    if summ == n:
        print(n,"=", end=' ')
        for j in range(len(factor)-1):
            print(factor[j], end=' + ')
        print(factor[j+1])

    else:
        print(n, "is NOT perfect.")

