from typing import Optional
import random
from games.KnockAbout.action import KnockaboutAction
from games.KnockAbout.result import KnockaboutResult
from games.state import State


class TictactoeState(State):
    EMPTY_CELL = 0

    def __init__(self, num_rows: int = 10, num_cols: int = 11):
        super().__init__()
        """
        the dimensions of the board
        """
        self.__num_rows = num_rows
        self.__num_cols = num_cols

        """
        the grid
        """
        self.__grid = [
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "183", "   ", "183", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "162", "   ", "162", "   ", "162", "   ", "   ", "   "],
            ["   ", "   ", "141", "   ", "141", "   ", "141", "   ", "141", "   ", "   "],
            ["   ", "   ", "041", "   ", "041", "   ", "041", "   ", "041", "   ", "   "],
            ["   ", "   ", "   ", "062", "   ", "062", "   ", "062", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "083", "   ", "083", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
            ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
        ]
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

    gutter_players = [[0] for row in range(2)]

    def __check_winner(self, player, state: State):

        current_player = state.get_acting_player
        
        if self.gutter_players[current_player] >= 5:
            return True
        
        return False


    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2

    def validate_position(self, action: KnockaboutAction) -> bool:
        col = action.get_col()
        row = action.get_row()

        # valid column
        if col < 0 or col >= self.__num_cols:
                return False
        
        # valid row
        if row < 0 or row >= self.__num_rows:
            return False
        
        # full row and col
        if self.__grid[row][col] == TictactoeState.EMPTY_CELL:
            return False

        return True
    
    def validate_direction(self, action: KnockaboutAction) -> bool:
        dir = action.get_dir()

        # check if direction is valid
        if dir not in ['left', 'right', 'up', 'down']:
            return False

        return True


    def update(self, action: KnockaboutAction):
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
        cell_value = self.__grid[row][col]

        # look for whom the dice belongs to, B for player 2 and P for player 1

        match cell_value[0]:
            case '0':
                print(' P', end="")
            case '1':
                print(' B', end="")

        # the type of dice and it's respective holding value

        match cell_value[1]:
            case '4':
                print(f'4{cell_value[2]} ', end="")
            case '6':
                print(f'6{cell_value[2]} ', end="")
            case '8':
                print(f'8{cell_value[2]} ', end="")
            case _:
                print('     ', end="")

    def __display_numbers(self):
        for col in range(0, self.__num_cols):
            if col < 10:
                print(' ', end="")
            print(col, end="")
        print("")

    def __display_separator(self):
        for col in range(0, self.__num_cols + 1):
            print("------", end="")
        print("-")

    def __display_number_column(self):
        for col in range(0, self.__num_cols + 1):
            print(f'    {col + 1} ', end="")
        print("")

    def display(self):
        self.__display_numbers()
        self.__display_number_column()
        self.__display_separator()

        for row in range(0, self.__num_rows + 1):
            print(f'{row + 1}|', end="")
            for col in range(0, self.__num_cols + 1):
                self.__display_cell(row, col)
                print('|', end="")
            print("")
            self.__display_separator()

        self.__display_numbers()
        print("")

   
    def is_finished(self) -> bool:
        return self.__has_winner

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

    def get_result(self, pos) -> Optional[KnockaboutResult]:
        if self.__has_winner:
            return KnockaboutResult.LOOSE if pos == self.__acting_player else KnockaboutResult.WIN
        if self.__is_full():
            return KnockaboutResult.DRAW
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
            lambda pos: KnockaboutAction(pos // self.get_num_cols(), pos % self.get_num_cols()),
            range(0, self.get_num_cols() * self.get_num_rows())
        )
    ))

    def find_pieces_on_the_way(self):
        pass

    def move_piece(self, action: KnockaboutAction):
        direction = action.get_dir()
        col = action.get_col()
        row = action.get_row()
        position = [row][col]
        value = self.__grid[row][col][2]
        piece_on_the_way = self.find_pieces_on_the_way()

        
        if direction == 'left':
            new_position = position[row - value][col]
        if direction == 'right':
            new_position = position[row + value][col]
        if direction == 'up':
            new_position = position[row][col + value]
        if direction == 'down':
            new_position = position[row][col - value]

        if piece_on_the_way is not None:
            new_position = piece_on_the_way

        return new_position
    
    

    def change_dice_value(self,row,col):
        cell_value = self.__grid[row][col]
        
        # define a limit and randomize and return a value
        limit = int(cell_value[1])
        new_value = random.randint(1,limit)

        #put that new value into the grid
        cell_value[2] = str(new_value)
        self.__grid[row][col] = cell_value

    def gutter_check(self, row,col):
        return row in [0, 9] or col in [0, 10]
    
    # 
    def gutter_add(self):
        aux_row = 0
        aux_col = 0

        # check the rows
        for aux_row in [0,9]:
            for aux_col in range(11):
                match self.__grid[aux_row][aux_col][0]:
                    # the values in gutter_players is inverted due to the acting player only winning if the other player looses
                    case 0:
                        self.gutter_players[1] += 1
                    case 1:
                        self.gutter_players[0] += 1    
        # check the collums
        for aux_row in range(11):
            for aux_col in [1,9]:
                match self.__grid[aux_row][aux_col][0]:
                    # the values in gutter_players is inverted due to the acting player only winning if the other player looses
                    case 0:
                        self.gutter_players[1] += 1
                    case 1:
                        self.gutter_players[0] += 1 




    def sim_play(self, action):
        new_state = self.clone()
        new_state.play(action)
        return new_state
