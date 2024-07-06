from static import AgentType, SYMBOLS


def create_agent(agent_type: AgentType, agent_index: int):
    if agent_type == AgentType.HUMAN:
        return HumanAgent(agent_index)


class HumanAgent:

    def __init__(self, id: int) -> None:
        self.id = id

    def valid_move(self, board, idx) -> bool:
        return idx in board.get_possible_moves()


    # def get_move(self,  board_state: List[int], idx: int):
    #     if self.valid_move(board_state, idx):
    #         return False
    #     tile_label.config(text=SYMBOLS[self.id])

