from node import Node

NYT = "NYT"


def switch_nodes(left_node: Node, right_node: Node):
    # switch references to the left node
    left_node.left, right_node.left = right_node.left, left_node.left

    # switch references to the right node
    left_node.right, right_node.right = right_node.right, left_node.right

    # switch contained symbols
    left_node.symbol, right_node.symbol = left_node.symbol, right_node.symbol


def print_code(root: Node, symbol):
    nodes_to_check = [root]
    code_for_new_symbol = ""

    while len(nodes_to_check) > 0:
        current_node = nodes_to_check.pop()

        if current_node.symbol == symbol:
            # returns code and false if it is not a new symbol on a tree
            return (current_node.code, False)
        if current_node.symbol == NYT:
            code_for_new_symbol = current_node.code
        if current_node.left:
            current_node.left.code = current_node.code + '0'
            nodes_to_check.append(current_node.left)
        if current_node.right:
            current_node.right.code = current_node.code + '1'
            nodes_to_check.append(current_node.right)

    # returns code for a new symbok and true if it is a new symbol on a tree
    return (current_node.code, True)


def update(root: Node, symbol, first_apperance):
    current_node = None
    while True:
        if first_apperance:
            current_node = find_node_symbol(root, NYT)
            current_node.right = Node(1, symbol)
            current_node.left = Node(0, NYT)
            current_node.weight += 1
            current_node.symbol = None
            current_node.left.parent = current_node
        else:
            if not current_node:
                current_node = find_node_symbol(root, symbol)

    return


def find_node_symbol(root: Node, symbol) -> Node:

    if root.symbol == symbol:
        return root

    if root.left != None:
        node = find_node_symbol(root.left, symbol)
        if node != None:
            return node

    if root.right != None:
        node = find_node_symbol(root.right, symbol)
        if node != None:
            return node

    return None
# te funkcje można połączyć w jedno ^v


def find_node_weight(root: Node, weight) -> Node:

    if root.weight == weight:
        return root

    if root.left != None:
        node = find_node_weight(root.left, weight)
        if node != None:
            return node

    if root.right != None:
        node = find_node_weight(root.right, weight)
        if node != None:
            return node

    return None
