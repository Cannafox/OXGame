from typing import List, Union
from agents import create_agent
from static import GameStatus


class Game:
    def __init__(self, player_1, player_2) -> None:
        self.player_1 = create_agent(player_1, 1)
        self.player_2 = create_agent(player_2, 2)
        self.status = GameStatus.RUNNING

        self.current_player = self.player_1

    def make_move(self, board, move_idx: int) -> Union[int, bool]:
        if self.status != GameStatus.RUNNING:
            return False
        if not self.current_player.valid_move(board, move_idx):
            return False
        return self.change_turn()

    def change_turn(self):
        if self.current_player.id == self.player_1.id:
            self.current_player = self.player_2
            return self.player_1.id
        else:
            self.current_player = self.player_1
            return self.player_2.id
    # def turn(self, board) -> :
    #     if self.status == GameStatus.RUNNING:
    #         player_move = self.current_player.get_move(board.get_possible_moves())



class Board:

    def __init__(self) -> None:
        self.reset()

    def set_state(self, idx: int, val: int) -> None:
        self.state[idx] = val

    def get_possible_moves(self) -> List[int]:
        possible_moves = [index for index in range(len(self.state)) if self.state[index] == 0]

        return possible_moves

    def reset(self) -> None:
        self.state = [0] * 9

    def get_state(self) -> List[int]:
        return self.state

    def __call__(self) -> List[int]:
        return self.get_state()

