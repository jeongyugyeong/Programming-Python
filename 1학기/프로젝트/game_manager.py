from tictactoe import TicTacToe

class GameManager:
    def __init__(self):
        self.ttt = TicTacToe()

    def play(self):
        # show_board()
        print(self.ttt)
        # 반복
        while True:
            # 위치를 입력받자
            row = int(input("row: "))
            col = int(input("col: "))
            # 말을 놓자
            self.ttt.set(row, col)
            # check_winner()
            print.self
            # 결과를 출력하자
            if self.ttt.check_winner() == "O":
                print("0 승리, 축하함미당")
                break
            elif self.ttt.check_winner() == "X":
                print("X 승리, 축하함미당")
                break
            elif self.ttt.check_winner() == "d":
                print("무승부")
                break

if __name__ == '__main__':
    gm = GameManager()
    gm.play()