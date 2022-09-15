board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    stack = []
    for i in moves:
        k = i-1
        for j in range(len(board)):
            if board[j][k] == 0:
                pass
            else:
                stack.append(board[j][k])
                board[j][k] = 0
                break
        if len(stack)>1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer+=2


    return answer






solution(board, moves)