from random import randint

from games.tictactoe.action import TictactoeAction
from games.tictactoe.player import TictactoePlayer
from games.tictactoe.state import TictactoeState
from games.state import State


class RandomTictactoePlayer(TictactoePlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: TictactoeState):
        return TictactoeAction(randint(0, state.get_num_cols()), randint(0, state.get_num_rows()))

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
