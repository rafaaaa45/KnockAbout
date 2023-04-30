from games.KnockAbout.action import KnockaboutAction
from games.KnockAbout.player import TictactoePlayer
from games.KnockAbout.state import TictactoeState


class HumanTictactoePlayer(TictactoePlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: TictactoeState):
        state.display()
        while True:
            # noinspection PyBroadException
            try:
                row = int(input(f"Player {state.get_acting_player()}, choose the row of the piece: "))
                col = int(input(f"Player {state.get_acting_player()}, choose the column of the piece: "))
                if state.validate_position((row, col)):
                    direction = input(f"Player {state.get_acting_player()}, choose the direction to move (up/down/left/right): ")
                    if state.validate_direction(direction):
                        return KnockaboutAction((row, col), direction)
                    else:
                        print("Invalid direction. Please choose a valid direction.")
                        continue
                else:
                    print("Invalid position. Please choose a valid position.")
                    continue
            except Exception:
                continue



    def event_action(self, pos: int, action, new_state: TictactoeState):
        # ignore
        pass

    def event_end_game(self, final_state: TictactoeState):
        # ignore
        pass
