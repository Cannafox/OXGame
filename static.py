from enum import Enum

RESOLUTION = (400, 300)
SYMBOLS = (".", "O", "X")

class AgentType(Enum):
    HUMAN = 0

class StatusCode(Enum):
    SUCCESS = 0
    FAIL = -1

class GameStatus(Enum):
    RUNNING = 0
    WIN = 1
    TIE = 2
class Stage(Enum):
    MENU = 0
    GAME = 1
    END_SCREEN = 2
