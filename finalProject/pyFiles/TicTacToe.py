import tkinter as tk
from itertools import cycle
from tkinter import font
from typing import NamedTuple
import random
import copy


class Player(NamedTuple):
    label: str
    color: str


class Move(NamedTuple):
    row: int
    col: int
    label: str = ""


BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label="X", color="blue"),
    Player(label="O", color="green"),
)


class TicTacToeGame:
    def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self._players = cycle(players)
        self.board_size = board_size
        self.current_player = next(self._players)
        self.winner_combo = []
        self._current_moves = []
        self._has_winner = False
        self._winning_combos = []
        self._setup_board()

    def _setup_board(self):
        self._current_moves = [
            [Move(row, col) for col in range(self.board_size)]
            for row in range(self.board_size)
        ]
        self._winning_combos = self._get_winning_combos()

    def _get_winning_combos(self):
        rows = [
            [(move.row, move.col) for move in row]
            for row in self._current_moves
        ]
        columns = [list(col) for col in zip(*rows)]
        first_diagonal = [row[i] for i, row in enumerate(rows)]
        second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]
        return rows + columns + [first_diagonal, second_diagonal]

    def toggle_player(self):
        """Возвращение хода."""
        self.current_player = next(self._players)

    def is_valid_move(self, move):
        """Разрешен ли следующий ход."""
        row, col = move.row, move.col
        move_was_not_played = self._current_moves[row][col].label == ""
        no_winner = not self._has_winner
        return no_winner and move_was_not_played

    def process_move(self, move):
        """Следующий ход и его проверка на победность."""
        row, col = move.row, move.col
        self._current_moves[row][col] = move
        for combo in self._winning_combos:
            results = set(self._current_moves[n][m].label for n, m in combo)
            is_win = (len(results) == 1) and ("" not in results)
            if is_win:
                self._has_winner = True
                self.winner_combo = combo
                break

    def has_winner(self):
        """Проверка наличия победителя."""
        return self._has_winner

    def is_tied(self):
        """Проверка ничьи."""
        no_winner = not self._has_winner
        played_moves = (
            move.label for row in self._current_moves for move in row
        )
        return no_winner and all(played_moves)

    def reset_game(self):
        """Сброс игры."""
        for row, row_content in enumerate(self._current_moves):
            for col, _ in enumerate(row_content):
                row_content[col] = Move(row, col)
        self._has_winner = False
        self.winner_combo = []

    def computer_move(self):
        """Улучшенный алгоритм для хода компьютера."""
        # Сначала создадим копию текущего состояния игры
        game_copy = copy.deepcopy(self)
        # 1. Если компьютер может выиграть, сделаем этот ход
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self._current_moves[i][j].label == "":
                    game_copy._current_moves[i][j] = Move(i, j, self.current_player.label)
                    if game_copy.has_winner():
                        return Move(i, j, self.current_player.label)
                    else:
                        game_copy._current_moves[i][j] = Move(i, j)

        # 2. Если игрок может выиграть, блокируем его
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self._current_moves[i][j].label == "":
                    game_copy._current_moves[i][j] = Move(i, j, self._get_opponent().label)
                    if game_copy.has_winner():
                        return Move(i, j, self.current_player.label)
                    else:
                        game_copy._current_moves[i][j] = Move(i, j)

        # 3. В противном случае сделаем случайный ход
        empty_cells = [(i, j) for i in range(self.board_size) for j in range(self.board_size) if
                       self._current_moves[i][j].label == ""]
        if empty_cells:
            move = random.choice(empty_cells)
            return Move(move[0], move[1], self.current_player.label)
        return None

    def _get_opponent(self):
        """Получить игрока-противника."""
        return next(player for player in DEFAULT_PLAYERS if player != self.current_player)


class TicTacToeBoard(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        self._cells = {}
        self._game = game
        self._create_menu()
        self._create_board_display()
        self._create_board_grid()

    def _create_menu(self):
        menu_bar = tk.Menu(master=self)
        self.config(menu=menu_bar)
        file_menu = tk.Menu(master=menu_bar)
        file_menu.add_command(label="Play Again", command=self.reset_board)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Готовы?",
            font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()

    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(self._game.board_size):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(self._game.board_size):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue",
                )
                self._cells[button] = (row, col)
                button.bind("<ButtonPress-1>", self.play)
                button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def play(self, event):
        """Ход игрока."""
        clicked_btn = event.widget
        row, col = self._cells[clicked_btn]
        move = Move(row, col, self._game.current_player.label)
        if self._game.is_valid_move(move):
            self._update_button(clicked_btn)
            self._game.process_move(move)
            if self._game.is_tied():
                self._update_display(msg="Ничья!", color="red")
            elif self._game.has_winner():
                self._highlight_cells()
                msg = f'Игрок "{self._game.current_player.label}" победил!'
                color = self._game.current_player.color
                self._update_display(msg, color)

                # Изменение: Если текущий игрок - крестик (X), не менять символы
                if self._game.current_player.label == "X":
                    self._game.reset_game()

            else:
                self._game.toggle_player()
                msg = f"Ход {self._game.current_player.label}'ка"
                self._update_display(msg)

                # После хода человека, проверим, не закончилась ли игра
                if not self._game.is_tied() and not self._game.has_winner():
                    # Если игра не закончена, тогда сделаем ход компьютера
                    computer_move = self._game.computer_move()
                    if computer_move:
                        self._update_button(self._get_button_for_move(computer_move))
                        self._game.process_move(computer_move)
                        if self._game.is_tied():
                            self._update_display(msg="Ничья!", color="red")
                        elif self._game.has_winner():
                            self._highlight_cells()
                            msg = f'Игрок "{self._game.current_player.label}" победил!'
                            color = self._game.current_player.color
                            self._update_display(msg, color)
                        else:
                            self._game.toggle_player()
                            msg = f"Ход {self._game.current_player.label}'ка"
                            self._update_display(msg)

    def _update_button(self, clicked_btn):
        clicked_btn.config(text=self._game.current_player.label)
        clicked_btn.config(fg=self._game.current_player.color)

    def _update_display(self, msg, color="black"):
        self.display["text"] = msg
        self.display["fg"] = color

    def _highlight_cells(self):
        for button, coordinates in self._cells.items():
            if coordinates in self._game.winner_combo:
                button.config(highlightbackground="red")

    def reset_board(self):
        """Сброс доски"""
        self._game.reset_game()
        self._update_display(msg="Готовы?")
        for button in self._cells.keys():
            button.config(highlightbackground="lightblue")
            button.config(text="")
            button.config(fg="black")

    def _get_button_for_move(self, move):
        for button, coordinates in self._cells.items():
            if coordinates == (move.row, move.col):
                return button
        return None


def main():
    game = TicTacToeGame()
    board = TicTacToeBoard(game)
    board.mainloop()


if __name__ == "__main__":
    main()
