class KnockaboutAction:
    """
    a connect 4 action is simple - it only takes the value of the column to play
    """
    __col: int
    __row: int
    __dir: str

    def __init__(self, col: int, row: int, direction: str):
        self.__col = col
        self.__row = row
        self.__dir = direction

    def get_col(self):
        return self.__col
    
    def get_row(self):
        return self.__row
    
    def get_dir(self):
        return self.__dir
