def solution(board, moves):
    answer = 0
    basket = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] != 0:
                basket.append(board[i][move - 1])
                board[i][move - 1] = 0
                break
        if len(basket) > 1 and basket[-1] == basket[-2]:
            answer += 2
            basket = basket[:-2]

    return answer