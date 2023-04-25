from games.tictactoe.action import TictactoeAction
from games.tictactoe.player import TictactoePlayer
from games.tictactoe.state import TictactoeState


class HumanTictactoePlayer(TictactoePlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: TictactoeState):
        state.display()
        while True:
            # noinspection PyBroadException
            try:
                return TictactoeAction(int(input(f"Player {state.get_acting_player()}, choose a column: ")), int(input(f"Player {state.get_acting_player()}, choose a row: ")))
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: TictactoeState):
        # ignore
        pass

    def event_end_game(self, final_state: TictactoeState):
        # ignore
        pass
