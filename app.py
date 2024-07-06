import tkinter as tk
import itertools
from tkinter import ttk
from typing import Union

from static import Stage, RESOLUTION, AgentType, SYMBOLS
from game import Game, Board

HEIGHT, WIDTH = RESOLUTION


class MenuScreen(tk.Frame):

    def __init__(self, parent, game):
        super().__init__(parent)
        self.game = game

        self.label = ttk.Label(self, text="MENU", font=("Arial", 30))
        self.label.pack(pady=20)

        self.start_button = ttk.Button(self,
                                       text="Start",
                                       command=parent.start_game)
        self.start_button.pack(pady=5)
        self.exit_button = ttk.Button(self, text="Exit", command=parent.quit)
        self.exit_button.pack(pady=5)

    def start_game(self) -> None:
        self.pack_forget()
        self.game.start_game()


class GameScreen(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.header = ttk.Label(self, text="GAME", font=("Arial", 30))
        self.header.grid(row=0, column=1)
        # self.label.pack(pady=20)

        self.board = Board()
        # print(self.board.get_possible_moves())
        # print(self.board)
        self.game = Game(player_1=AgentType.HUMAN, player_2=AgentType.HUMAN)

        self.update()

    @staticmethod
    def coord_to_idx(row: int, col: int) -> int:
        return 3 * row + col % 3

    def on_label_click(self, _, idx: int) -> None:
        print(idx)
        current_move = self.game.make_move(self.board, idx)
        if current_move:
            self.board.set_state(idx, val=current_move)
            self.update()


    def update(self):
        self.tile_labels = []
        print(self.board)
        for row, col in itertools.product([1, 2, 3], [1, 2, 3]):
            idx = self.coord_to_idx(row=row-1, col=col-1)
            symbol = SYMBOLS[self.board.get_state()[idx]]

            tile_label = tk.Label(self, text=symbol, font=("Arial", 30)) #
            tile_label.grid(row=row, column=col)
            tile_label.bind('<Button>', lambda event, idx=idx: self.on_label_click(event, idx))

            self.tile_labels.append(tile_label)
        self.footer = ttk.Label(self, text=f"{SYMBOLS[self.game.current_player.id]} turn")
        self.footer.grid(row=4, column=1)


    def start_game(self) -> None:
        self.pack()


class EndScreen(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('OX Game')
        self.geometry(f'{WIDTH}x{HEIGHT}')

        self.menu=MenuScreen(self, self)
        self.menu.pack()
        self.game=GameScreen(self)
        self.end_screen=EndScreen(self)

        self.current_stage=Stage.MENU  # Stage.MENU

    def get_current_stage(self) -> Union[MenuScreen, GameScreen, EndScreen]:
        if self.current_stage == Stage.MENU:
            return self.menu
        elif self.current_stage == Stage.GAME:
            return self.game

        return self.end_screen

    def start_game(self) -> None:
        self.change_stage(Stage.GAME)

    def change_stage(self, stage: Stage) -> None:
        self.get_current_stage().pack_forget()
        self.current_stage=stage
        self.get_current_stage().pack()
