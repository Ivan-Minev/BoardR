from board_item import BoardItem

class Board:
    def __init__(self, input_items=list[BoardItem]):
        self.items = []
        self.input_items = input_items