arr1 = [[1, 2], [2, 3]]
arr2 = [[3,4], [5, 6]]

def solution(arr1, arr2):
    for i in range(len(arr2)):
        for j in range(len(arr2[i])):
            arr1[i][j] += arr2[i][j]
    
    return arr1

#zip()사용시 index로 리스트를 굳이 명시적으로  순환할 필요없음 알아서 처리해줌
def solve(arr1, arr2):
    arr1 = [[c+d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
    return arr1

print(solve(arr1, arr2))
