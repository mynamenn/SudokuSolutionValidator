def validator(board):
    size=len(board)
    sumCol=0
    counter=0
    sumSq =0
    startPos=0
    
    if 0 in board:  
        return False
    
    for row in range(size):                
        if sum(board[row]) !=45:        #check if sum of each row =45
            return False
            break 
        sumCol=0
        for col in range(size):         #check if sum of each col =45
            sumCol += board[col][row]
        if sumCol != 45:
            return False
            break
            
    for a in range(6,-3,-3):
        sumSq =0
        for row in range(startPos, size-a): 
            for col in range(startPos, size-a):
                sumSq += board[row][col]     #check if sum of each square =45
        if sumSq != 45:
             return False
             break
        startPos +=3     
    
    return True
