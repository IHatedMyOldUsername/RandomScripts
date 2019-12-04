theBoard = {'TL':' ', 'TM':' ', 'TR':' ',
            'ML':' ', 'MM':' ', 'MR':' ',
            'BL':' ', 'BM':' ', 'BR':' '}

def printBoard(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-+')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-+')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    
printBoard(theBoard)
