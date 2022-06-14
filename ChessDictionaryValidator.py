# Checks whether a given dictionary has a valid chess board-state:
# 1 king of each color
# At most 8 pawns of each color
# At most 15 non-king pieces of each color
# Contains only valid piece names
# Contains only valid spaces
# 1 piece per space

def chessValidCheck(board):
    valid = True
    VALIDPIECES = ['wPawn', 'wKnight', 'wBishop', 'wRook', 'wQueen', 'wKing', 'bPawn', 'bKnight', 'bBishop', 'bRook', 'bQueen', 'bKing']

    
    # Check number of pieces of each color
    blackPawnCt = 0
    whitePawnCt = 0
    blackKingCt = 0
    whiteKingCt = 0
    whiteNonKingCt = 0
    blackNonKingCt = 0
    for piece in board.values():
        if piece not in VALIDPIECES:
            valid = False
            break
        if piece == 'bPawn':
            blackPawnCt += 1
        if piece == 'wPawn':
            whitePawnCt += 1
        if piece == 'bKing':
            blackKingCt += 1
        if piece == 'wKing':
            whiteKingCt += 1
        if piece != 'bKing' and piece != 'wKing':
            if piece[0] == 'b':
                blackNonKingCt += 1
            else:
                whiteNonKingCt += 1
    
    if (blackPawnCt > 8) or (whitePawnCt > 8) or (blackKingCt != 1) or (whiteKingCt != 1) or (blackNonKingCt > 15) or (whiteNonKingCt > 15):
        valid = False


    # Check for valid spaces and # of pieces per space = 1
    for space in board.keys():
        if len(space) != 2:
            valid = False
        if space[0] not in ['a','b','c','d','e','f','g','h']:
            valid = False
        if space[1] not in ['1','2','3','4','5','6','7','8']:
            valid = False
        
        # No need to check number of pieces per space, would throw an error if non-unique keys
    return valid
            
# Valid board
print(chessValidCheck({'h1': 'bKing', 'c6': 'wQueen', 'g2': 'bBishop', 'h5': 'bQueen', 'e3': 'wKing'}))

# Invalid - no bKing
print(chessValidCheck({'c6': 'wQueen', 'g2': 'bBishop', 'h5': 'bQueen', 'e3': 'wKing'}))

# Invalid - two bKing
print(chessValidCheck({'h1': 'bKing', 'h2': 'bKing', 'c6': 'wQueen', 'g2': 'bBishop', 'h5': 'bQueen', 'e3': 'wKing'}))

# Invalid - 9 pawns
print(chessValidCheck({'h1': 'bKing', 'c6': 'wQueen', 'g2': 'bBishop', 'h5': 'bQueen', 'e3': 'wKing', 'f1': 'bPawn', 'f2': 'bPawn', 'f3': 'bPawn', 'f4': 'bPawn', 'f5': 'bPawn', 'f6': 'bPawn', 'f7': 'bPawn', 'f8': 'bPawn', 'h8': 'bPawn'}))

# Invalid - fake space
print(chessValidCheck({'z1': 'bKing', 'c6': 'wQueen', 'g2': 'bBishop', 'h5': 'bQueen', 'e3': 'wKing'}))