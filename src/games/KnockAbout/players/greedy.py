from random import choice
from games.tictactoe.action import KnockaboutAction
from games.tictactoe.player import TictactoePlayer
from games.tictactoe.state import TictactoeState
from games.state import State


class GreedyTictactoePlayer(TictactoePlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: TictactoeState):
        # obtém a grade
        grid = state.get_grid()
        #scoluna e linha selecionadas
        selected_col = None
        selected_row = None
        max_count = 0

        #percorre todas as col/row
        for col in range(0, state.get_num_cols()):
            for row in range(0, state.get_num_rows()):
                #verifica se ação válida
                if not state.validate_action(KnockaboutAction(col,row)):
                    continue
                
                count = 0
                #conta o número de joga
                if grid[row][col] == self.get_current_pos():
                    count += 1

                # seleciona a jogada com base na contagem atual
                # atualiza a jogada selecionada para a jogada atual
                if selected_col is None or count > max_count or (count == max_count and choice([False, True])):
                    if selected_row is None or count > max_count or (count == max_count and choice([False, True])):
                        selected_col = col
                        selected_row = row
                        max_count = count
        # se nenhuma jogada válida
        if selected_col is None:
            raise Exception("There is no valid action")

        return KnockaboutAction(selected_col, selected_row)

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass