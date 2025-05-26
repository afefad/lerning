# 1. Класс, который будет описывать одну клетку поля:
class Cell:
    def __init__(self, index):
        self.index = index  # Номер клетки от 1 до 9
        self.occupied_by = None  # None, 'X' или 'O'

    def is_free(self):
        return self.occupied_by is None

    def __str__(self):
        return self.occupied_by if self.occupied_by else str(self.index)

# 2. Класс, который будет описывать поле игры.
class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def display(self):
        print("\nТекущее поле:")
        for i in range(0, 9, 3):
            row = " | ".join(str(self.cells[i + j]) for j in range(3))
            print(row)
            if i < 6:
                print("-" * 9)

    def reset(self):
        for cell in self.cells:
            cell.occupied_by = None

    def make_move(self, index, symbol):
        if 1 <= index <= 9 and self.cells[index - 1].is_free():
            self.cells[index - 1].occupied_by = symbol
            return True
        return False

    def is_full(self):
        return all(not cell.is_free() for cell in self.cells)

    def check_win(self, symbol):
        win_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # горизонтали
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # вертикали
            (0, 4, 8), (2, 4, 6)              # диагонали
        ]
        for a, b, c in win_combinations:
            if (self.cells[a].occupied_by == symbol and
                self.cells[b].occupied_by == symbol and
                self.cells[c].occupied_by == symbol):
                return True
        return False

# 3. Класс, который описывает поведение игрока:
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.score = 0

    def get_move(self):
        while True:
            try:
                move = int(input(f"{self.name} ({self.symbol}), введите номер клетки (1-9): "))
                if 1 <= move <= 9:
                    return move
                else:
                    print("Ошибка: нужно ввести число от 1 до 9.")
            except ValueError:
                print("Ошибка: введите корректное число.")

# 4. Класс, который управляет ходом игры:
class Game:
    def __init__(self):
        self.board = Board()
        self.players = []

    def single_turn(self, player):
        self.board.display()
        while True:
            move = player.get_move()
            if self.board.make_move(move, player.symbol):
                break
            print("Эта клетка уже занята, выберите другую.")

        if self.board.check_win(player.symbol):
            self.board.display()
            print(f"\nПобеда игрока {player.name}!")
            player.score += 1
            return True
        return False

    def single_game(self):
        self.board.reset()
        turn = 0
        while not self.board.is_full():
            current_player = self.players[turn % 2]
            if self.single_turn(current_player):
                return True
            turn += 1
        self.board.display()
        print("\nНичья!")
        return False

    def main_loop(self):
        name1 = input("Введите имя первого игрока (X): ")
        name2 = input("Введите имя второго игрока (O): ")
        self.players = [Player(name1, "X"), Player(name2, "O")]

        while True:
            print("\n--- Новая игра ---")
            self.single_game()

            print(f"\nСчёт: {self.players[0].name} {self.players[0].score} - {self.players[1].score} {self.players[1].name}")
            again = input("Хотите сыграть ещё раз? (д/н): ").strip().lower()
            if again != 'д':
                print("Спасибо за игру!")
                break

game = Game()
game.main_loop()
