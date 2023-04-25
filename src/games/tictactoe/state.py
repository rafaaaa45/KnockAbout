from typing import Optional

from games.tictactoe.action import TictactoeAction
from games.tictactoe.result import TictactoeResult
from games.state import State


class TictactoeState(State):
    EMPTY_CELL = -1

    def __init__(self, num_rows: int = 3, num_cols: int = 3):
        super().__init__()

        if num_rows != 3:
            raise Exception("the number of rows must be 3")
        if num_cols != 3:
            raise Exception("the number of cols must be 3")

        """
        the dimensions of the board
        """
        self.__num_rows = num_rows
        self.__num_cols = num_cols

        """
        the grid
        """
        self.__grid = [[TictactoeState.EMPTY_CELL for _i in range(self.__num_cols)] for _j in range(self.__num_rows)]

        """
        counts the number of turns in the current game
        """
        self.__turns_count = 1

        """
        the index of the current acting player
        """
        self.__acting_player = 0

        """
        determine if a winner was found already 
        """
        self.__has_winner = False

    def __check_winner(self, player):
    # check for 3 across
        for row in range(0, self.__num_rows):
            if self.__grid[row][0] == player and \
            self.__grid[row][1] == player and \
            self.__grid[row][2] == player:
                return True

        # check for 3 up and down
        for col in range(0, self.__num_cols):
            if self.__grid[0][col] == player and \
            self.__grid[1][col] == player and \
            self.__grid[2][col] == player:
                return True

        # check upward diagonal
        if self.__grid[0][0] == player and \
        self.__grid[1][1] == player and \
        self.__grid[2][2] == player:
            return True

        # check downward diagonal
        if self.__grid[2][0] == player and \
        self.__grid[1][1] == player and \
        self.__grid[0][2] == player:
            return True


        return False


    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2

    def validate_action(self, action: TictactoeAction) -> bool:
        col = action.get_col()
        row = action.get_row()

        # valid column
        if col < 0 or col >= self.__num_cols:
            return False
        
        # valid row
        if row < 0 or row >= self.__num_rows:
            return False
        
        # full row and col
        if self.__grid[row][col] != TictactoeState.EMPTY_CELL:
            return False

        return True

    def update(self, action: TictactoeAction):
        col = action.get_col()
        row = action.get_row()

        # player play
        self.__grid[row][col] = self.__acting_player

        # determine if there is a winner
        self.__has_winner = self.__check_winner(self.__acting_player)

        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0

        self.__turns_count += 1

    def __display_cell(self, row, col):
        print({
                  0: 'X',
                  1: 'O',
                  TictactoeState.EMPTY_CELL: ' '
              }[self.__grid[row][col]], end="")

    def __display_numbers(self):
        for col in range(0, self.__num_cols):
            if col < 10:
                print(' ', end="")
            print(col, end="")
        print("")

    def __display_separator(self):
        for col in range(0, self.__num_cols):
            print("--", end="")
        print("-")

    def display(self):
        self.__display_numbers()
        self.__display_separator()

        for row in range(0, self.__num_rows):
            print('|', end="")
            for col in range(0, self.__num_cols):
                self.__display_cell(row, col)
                print('|', end="")
            print("")
            self.__display_separator()

        self.__display_numbers()
        print("")

    def __is_full(self):
        return self.__turns_count > (self.__num_cols * self.__num_rows)

    def is_finished(self) -> bool:
        return self.__has_winner or self.__is_full()

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        cloned_state = TictactoeState(self.__num_rows, self.__num_cols)
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        for row in range(0, self.__num_rows):
            for col in range(0, self.__num_cols):
                cloned_state.__grid[row][col] = self.__grid[row][col]
        return cloned_state

    def get_result(self, pos) -> Optional[TictactoeResult]:
        if self.__has_winner:
            return TictactoeResult.LOOSE if pos == self.__acting_player else TictactoeResult.WIN
        if self.__is_full():
            return TictactoeResult.DRAW
        return None

    def get_num_rows(self):
        return self.__num_rows

    def get_num_cols(self):
        return self.__num_cols

    def before_results(self):
        pass

    def get_possible_actions(self):
        return list(filter(
        lambda action: self.validate_action(action),
        map(
            lambda pos: TictactoeAction(pos // self.get_num_cols(), pos % self.get_num_cols()),
            range(0, self.get_num_cols() * self.get_num_rows())
        )
    ))


    def sim_play(self, action):
        new_state = self.clone()
        new_state.play(action)
        return new_state
