from games.KnockAbout.player import TictactoePlayer
from games.KnockAbout.state import TictactoeState
from games.game_simulator import GameSimulator


class TictactoeSimulator(GameSimulator):

    def __init__(self, player1: TictactoePlayer, player2: TictactoePlayer, num_rows: int = 9, num_cols: int = 10):
        super(TictactoeSimulator, self).__init__([player1, player2])
        """
        the number of rows and cols from the connect4 grid
        """
        self.__num_rows = num_rows
        self.__num_cols = num_cols

    def init_game(self):
        return TictactoeState(self.__num_rows, self.__num_cols)

    def before_end_game(self, state: TictactoeState):
        # ignored for this simulator
        pass

    def end_game(self, state: TictactoeState):
        # state.display()
        # ignored for this simulator
        pass
