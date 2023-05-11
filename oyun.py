import os


class Connect_Four():

    COL_COUNT = 9
    ROW_COUNT = 9

    def __init__(self):
        self.board = [[' ' for i in range(Connect_Four.COL_COUNT)] for j in range(
            Connect_Four.ROW_COUNT)]

    def print_board(self, filename):
        with open(filename, "r") as f:
            print(f.read())

    def reset_board(self, filename):
        with open(filename, 'w') as f:
            f.write('')

    

    def print_board_to_file(self, filename):
        with open(filename, 'w') as f:
            result = ''
            result += '-' * 23
            for i in self.board:
                result += '\n'
                for j in i:
                    result += f'|{j}'
                result += '|\n'
            result += '-' * 23
            f.write(result)

    def drop(self, col, team: str):
        if col is None:
            print('Tur kaybettiniz.')
            return
        if not col.isdigit():
            print('Lütfen sayı giriniz.')
            return
        col = int(col)
        if col == 0:
            return
        if col < 1 or col > len(self.board[0]):
            print('1 den' +
                  str(len(self.board[0])) + ' ' +' a kadar bir sayı giriniz.')
            return
        col -= 1
        if self.board[0][col] == ' ':
            for i in range(len(self.board)-1, -1, -1):
                if self.board[i][col] == ' ':
                    self.board[i][col] = team
                    with open("Hamle.txt", "a") as f:
                        f.write(
                            f"{team} sembolune sahip takim : ({col+1}, {i}) konumuna pul birakti.\n")
                    break
            else:
                print(
                    'Kolon dolu, tur kaybettiniz.')
        else:
            print('Kolon dolu, tur kaybettiniz.')

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
    # Hamle.txt dosyasını her oyun başlangıcında temizliyoruz
    with open("Hamle.txt", "w") as f:
        f.write(f"")

    team1, team2 = '', ''
    print("CONNECT 4 OYUNUNA HOŞGELDİNİZ!")
    # Oyncuların sembollerini seçtiriyoruz, while döngüsü farklı karakter girilene kadar devam ediyor.
    while len(team1) != 1:
        team1 = input(
            '1.Oyuncu olarak tahtada kullanacağınız karakteri seçiniz: ')

    while len(team2) != 1 and team1 != team2:
        team2 = input(
            '2.Oyuncu olarak tahtada kullanacağınız karakteri seçiniz: ')
        while team2 == team1:
            print('Lütfen 1. oyuncunun seçtiğinden farklı bir karakter seçiniz!')
            team2 = input(
                '2.Oyuncu olarak tahtada kullanacağınız karakteri seçiniz: ')

    while not board.check(team1) and not board.check(team2):

        print("Menüye ulaşmak için '0' a basınız")

        col = input(
            f'1. oyuncu ({team1}) , lütfen bir kolona pul bırakınız. ')
        board.drop(col, team1)
        if col == "0":
            print("Menü Seçenekleri")
            print("a. Yeni Oyun")
            print("b. Kayıtlı Oyun")
            print("c. Oyunu Kaydet.")
            menu_input = input("a-b-c arasından seçiniz. ")

            if menu_input == "a":
                board = Connect_Four()
                continue

            elif menu_input == "b":
                
                print("Kayıtlı oyun başlatılıyor.")
                board.print_board("KayıtlıOyun.txt")
                

            elif menu_input == "c":
                # Handle save game
                print("Saving game...")
                board.print_board_to_file("KayıtlıOyun.txt")
                continue
        if col != "b" or "c":
            board.print_board_to_file("Tahta.txt")
            board.print_board("Tahta.txt")

            if board.check(team1):
                print(f'Oyuncu 1 ({team1}) kazandı!')
                quit()

            if board.check_tie():
                print('Berabere!')
                quit()
        print("Menüye ulaşmak için '0' a basınız")
        col = input(
            f'2. oyuncu ({team2}) , lütfen bir kolona pul bırakınız. ')
        board.drop(col, team2)
        if col == "0":
            print("Menü Seçenekleri")
            print("a. Yeni Oyun")
            print("b. Kayıtlı Oyun")
            print("c. Oyunu Kaydet.")
            menu_input = input("a-b-c arasından seçiniz. ")

            if menu_input == "a":
                board = Connect_Four()
                continue
                
            elif menu_input == "b":
               
                print("Kayıtlı oyun başlatılıyor.")
                board.print_board("KayıtlıOyun.txt")
                

            elif menu_input == "c":
                # Handle save game
                print("Oyun KayıtlıOyun.txt dosyasına kaydedildi.")
                board.print_board_to_file("KayıtlıOyun.txt")
                continue
            else:
                print("Geçersiz input. Tekrar deneyiniz.")
                continue
        
        board.print_board_to_file("Tahta.txt")
        board.print_board("Tahta.txt")

        if board.check(team2):
            print(f'Oyuncu 2  ({team2})kazandı!')
            quit()

        if board.check_tie():
            print('Berabere!')
            quit()
