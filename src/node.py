class Node:
    def __init__(self, weight: int, symbol):
        self.left = None
        self.right = None
        self.parent = None

        self.symbol = symbol
        self.weight = weight
        self.code = ""  # for printing purpose
