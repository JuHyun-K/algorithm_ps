'''
문제에서 준 배열을 재정렬해야 / 그대로 쓰면 O(n^2)도 가능
문제에서 받은 배열의 처음이 맨 위
https://kitle.xyz/post/95/
(https://kitle.xyz/post/95/)
'''
def makeNewBoard(board):
    n = len(board) #정사각 보드이므로
    bd = [[0] * n for i in range(n)]
    newBoard = []
    
    for i in range(n): #밑에서 부터 접근
        for j in range(n):
                bd[j][i] = board[i][j] #tranpose 행렬에서 x, y를 y,x 좌표로(그러면 [row][col] -> [col][row])가 
                
    for i in range(n): #0제
        tmp = []
        for j in range(n-1, -1, -1):
            if(bd[i][j] == 0):
                break
            tmp.append(bd[i][j])
        newBoard.append(tmp)
        
    return newBoard #뒤에서 부터가 맨 위
        
        
def solve(bd, moves):
    board = makeNewBoard(bd)
    stack = []
    count = 0
    top = -1
    
    for i in moves:
        #stack에 넣기
        if(len(board[i-1]) == 0): #각 행에 원소가 0이면 continue
            continue
        
        ele = board[i-1][-1] 
        del board[i-1][-1]
        stack.append(ele)
        top += 1
        
        #검사
        if(top == 0): #stack에 원소가 1개이
            continue
        if(stack[top-1] == stack[top]):
            del stack[top]
            del stack[top-1]
            count += 1
            top -= 2
            
    return count*2
        

def solution(board, moves):
    answer = solve(board, moves) #(board, moves)
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
[[0, 0, 0, 4, 3], [0, 0, 2, 2, 5], [0, 1, 5, 4, 1], [0, 0, 0, 4, 3], [0, 3, 1, 2, 1]]
moves = [1,5,3,5,1,2,1,4]
#moves = [0,4,2,4,0,1,0,3]
ans = solution(board, moves)
print(ans)
