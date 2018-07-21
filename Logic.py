#Ryan Cox ID# 31953949
#Class

class GameError(Exception):
    pass

##### OTHELLO CLASS #####

class OthelloClass:
    def __init__(self, board: [[list]], rows:int, columns:int, turn:str, how_its_won:str):
        self.row = rows
        self.col = columns
        self.turn = turn
        self.how_won = how_its_won
        self.board = board

##### PRIVATE FUNCTIONS TO CALL VARIABLES ######
    def _self_row(self) -> int:
        return self.row

    def _self_col(self) -> int:
        return self.col

    def _self_turn(self) -> str:
        return self.turn

    def _self_how_won(self) -> str:
        return self.how_won

    def _self_board(self) -> [[list]]:
        return self.board

##### FUNCTIONS #####

    # Board Stuff #

    def score(self) -> str:
        ''' counts up each tile for each color and returns score'''
        white_score = 0
        black_score = 0
        board = self._self_board()
        rows = self._self_row()
        columns = self._self_col()

        for i in range(rows):
            for j in range(columns):
                if board[j][i] == 'W':
                    white_score += 1
                elif board[j][i] == 'B':
                    black_score += 1
                else:
                    pass

        score = ("B: {}  W: {}".format(black_score, white_score))

        return score


    def _turn(self):
        ''' takes a player and changes the turn'''
        turn = self.turn
        if turn == 'W':
            return 'B'
        else:
            return  'W'

    def turn_output(self):
        ''' takes a player and returns the turn'''
        turn = self.turn
        if turn == 'W':
            return 'Turn: W'
        else:
            return 'Turn: B'

    def change_turn(self):
        ''' changes the turn'''
        self.turn = self._turn()


    def on_board(self, row:int, col:int) -> bool:
        ''' tests if a move is on the board'''
        if col >= 0 and col <= self._self_col() and row >= 0 and row <= self._self_row():
            return True
        else:
            return False

    def empty_spot(self, row:int, col:int) -> bool:
        ''' tests if the spot is empty'''
        board = self._self_board()
        
        if board[row][col] == '.':
            return True
        else:
            return False

#Moves
    def test_for_move(self):
        '''will test to see if white has any available moves '''
        moves = []
        test = [[0,1],[1,0],[0,-1],[-1,0],[-1,1],[1,-1],[-1,-1],[1,1]]
        turn = self.turn
        other_turn = ''
        if turn == 'B':
            other_turn = 'W'
        else:
            other_turn = 'B'
        board = self._self_board()

        for i in range(self.row):
            for j in range(self.col):
                for k in test:
                    
                    r = i
                    c = j
                    r += k[0]
                    c += k[1]
                    try:
                        if r < 0:
                            pass
                        elif c < 0:
                            pass
                        elif board[r][c] == turn:
                            pass
                        elif board[r][c] == other_turn:
                            moves.append([i,j])
                    except IndexError:
                        pass
        if moves != []:
            return True #white has moves
        else:
            return False

    def valid_moves(self) -> list:
        ''' ejects a list of valid moves for white'''
        moves = []
        test = [[0,1],[1,0],[0,-1],[-1,0],[-1,1],[1,-1],[-1,-1],[1,1]]
        turn = self.turn
        other_turn = ''
        if turn == 'B':
            other_turn = 'W'
        else:
            other_turn = 'B'
        board = self._self_board()

        for i in range(self.row):
            for j in range(self.col):
                if board[i][j] == '.':
                    for k in test:
                        r = i
                        c = j
                        r += k[0]
                        c += k[1]
                        if r > 0 and r < self.row and c > 0 and c < self.col:
                            if board[r][c] == other_turn:
                                moves.append([i,j])

        return moves

    def make_move(self, move_board: [[list]]):
        ''' allows white to make a move'''
        turn = self.turn
        other_turn = ''
        if turn == 'B':
            other_turn = 'W'
        else:
            other_turn = 'B'
        board = self._self_board()

        print(move_board)
        test = [[0,1],[1,0],[0,-1],[-1,0],[-1,1],[1,-1],[-1,-1],[1,1]]

        for i in range(len(move_board)):
            for j in range(len(move_board[i])):
                if move_board[i][j] == turn:
                    row = i
                    col = j

        

        flip = []

        possible_moves = self.valid_moves()

        if [row,col] in possible_moves:
            print("VALID")
            board[row][col] = turn
            for k in test:
                r = row
                c = col
                r += k[0]
                c += k[1]
                if r >= 0 and r < self.row and c >= 0 and c < self.col:
                    if board[r][c] == other_turn:
                        flip.append([r,c])
                    
                
        else:
            print("INVALID")
            self.make_move()

        for r, c in flip:
            board[r][c] = turn

#Game Over
    def game_over(self) -> bool:
        ''' determines if the game is over'''
        moves_left = 0
        board = self.board

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    moves_left += 1
                else:
                    moves_left += 0

        if moves_left > 0:
            return True #Moves left
        else:
            return False
    
    def game_over_output(self) -> str:
        ''' returns the winner'''
        board = self._self_board()
        black_score = 0
        white_score = 0
        how_won = self.how_won

        for i in range(self._self_row()):
            for j in range(self._self_row()):
                if board[i][j] == 'W':
                    white_score += 1
                elif board[i][j] == 'B':
                    black_score += 1
                else:
                    pass
        
        if how_won == '>':
            if black_score > white_score:
                return 'B'
            elif white_score > black_score:
                return 'W'
            else:
                return 'NONE'
        elif how_won == '<':
            if black_score < white_score:
                return 'B'
            elif white_score < black_score:
                return 'W'
            else:
                return 'NONE'
