class Node:
    def __init__(self, weight: int, symbol, number: int, parent = None):
        self.left = None
        self.right = None
        self.parent = parent

        self.symbol = symbol
        self.weight = weight
        self.number = number

        self.code = ""  # for printing purpose
