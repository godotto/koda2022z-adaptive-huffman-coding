class Node:
    def __init__(self, weight: int, depth: int, symbol):
        self.left = None
        self.right = None
        self.parent = None

        self.symbol = symbol
        self.weight = weight
        self.depth = depth
        self.code = ""  # for printing purpose
