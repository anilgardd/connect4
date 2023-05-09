import os

class Connect_Four():
    
    COL_COUNT = 9
    ROW_COUNT = 9


    def __init__(self):
        self.board = [[' ' for i in range(Connect_Four.COL_COUNT)] for j in range(
            Connect_Four.ROW_COUNT)]

    def print_board(self, filename=None):
        with open("tahta.txt", "r") as f:
            print(f.read())



    # def print_board(self):

    #     result = ''
    #     for i in self.board:
    #         result += '-' * 23 + '\n'
    #         for j in i:
    #             result += f'|{j}'
    #         result += '|\n'
    #     result += '-' * 23
    #     print(result)

    def print_board_to_file (self, filename):
        with open(filename,'w') as f:
            result=''
            result += '-' * 23 
            for i in self.board:
                result += '\n'
                for j in i:
                    result += f'|{j}'
                result+='|\n'
            result += '-' *23
            f.write(result)

    
    def drop(self, col, team: str):
        
        if col:
            if col.isdigit():
                col = int(col)
                if col < len(self.board[0]) and col > -1 or col == None:
                    col -= 1
                    if self.board[0][col] == ' ':
                        for i in range(len(self.board)-1, -1, -1):
                            if self.board[i][col] == ' ':
                                self.board[i][col] = team
                                with open("Hamle.txt", "a") as f:
                                    f.write(f"{team}: ({col}, {i})\n")
                                break
                        else:
                            print('That column is full dill weed. Look much? You\'ve lost your turn.')
                    else:
                        print('That column is full dill weed. Look much? You\'ve lost your turn.')
                else:
                    print('1... to... ' + str(len(self.board[0])) + '... dumbass... You lose your turn.')
            else:
                print('NUMBERS (WO)MAN! I NEED NUMBERS! Lose a turn.')
        else:
            print('... You have to enter something you troglodite. Lose a turn.')
        
    

            



  

    def check(self, team: str):

        # check horizontal wins
        for i in range(Connect_Four.COL_COUNT - 3):
            for j in range(Connect_Four.ROW_COUNT):
                if self.board[j][i] == team and self.board[j][i + 1] == team and self.board[j][i + 2] == team and \
                        self.board[j][i + 3] == team:
                    return True

        # check for vertical wins
        for c in range(Connect_Four.COL_COUNT):
            for r in range(Connect_Four.ROW_COUNT - 3):
                if self.board[r][c] == team and self.board[r + 1][c] == team and self.board[r + 2][c] == team and \
                        self.board[r + 3][c] == team:
                    return True

        # check for diagonal right wins (works)
        for c in range(Connect_Four.COL_COUNT-3):
            for r in range(Connect_Four.ROW_COUNT-3):
                if self.board[r][c] == team and self.board[r+1][c+1] == team and self.board[r+2][c+2] == team and self.board[r+3][c+3] == team:
                    return True

        # check for diagonal left wins (works)
        for c in range(Connect_Four.COL_COUNT-4, Connect_Four.COL_COUNT):
            for r in range(Connect_Four.ROW_COUNT-3):
                if self.board[r][c] == team and self.board[r+1][c-1] == team and self.board[r+2][c-2] == team and self.board[r+3][c-3] == team:
                    return True

    def check_tie(self):

        for i in self.board:
            for j in i:
                if j == ' ':
                    return False
        return True
    
        

   

if __name__ == '__main__':
    board = Connect_Four()
    board.print_board()

    team1, team2 = '', ''

    # Players enter the token they wish to use for the game, a token must not be longer than one character, and may not be the same
    while len(team1) != 1:
        team1 = input(
            'Enter a single character to use as your token player 1: ')

    while len(team2) != 1 and team1 != team2:
        team2 = input(
            'Enter a single character to use as your token player 2: ')
        if team2 == team1:
            print('Please choose a token different from player 1...  How ya gonna tell the difference in teams?  Dummy.')

    while not board.check(team1) and not board.check(team2):
        col = input(f'Player 1 ({team1}) insert piece in col (1-9): ')
        board.drop(col, team1)
        # board.print_board()
        # board.print_board_to_file("Tahta.txt")
        board.print_board_to_file("Tahta.txt")
        board.print_board("Tahta.txt")
        
        # last_move = board.last_move()
        # print(last_move)
        

        if board.check(team1):
            print(f'PLAYER 1 ({team1}) WINS!')
            quit()

        if board.check_tie():
            print('GAME TIED!  YOU BOTH LOSE!')
            quit()

        col = input(f'Player 2 ({team2}) insert piece in col (1-): ')
        board.drop(col, team2)

        # board.print_board()
        # board.print_board_to_file("Tahta.txt")
        board.print_board_to_file("Tahta.txt")
        board.print_board("Tahta.txt")

        # last_move = board.last_move()
        # print(last_move)
        

        if board.check(team2):
            print(f'PLAYER 2 ({team2}) WINS!')
            quit()

        if board.check_tie():
            print('GAME TIED!  YOU BOTH LOSE!')
            quit()
