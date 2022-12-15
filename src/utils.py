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
            return (current_node.code, False) # returns code and false if it is not a new symbol on a tree
        if current_node.symbol == NYT:
            code_for_new_symbol = current_node.code
        if current_node.left:
            current_node.left.code = current_node.code + '0'
            nodes_to_check.append(current_node.left)
        if current_node.right:
            current_node.right.code = current_node.code + '1'
            nodes_to_check.append(current_node.right)
        
    return (current_node.code, True) # returns code for a new symbok and true if it is a new symbol on a tree
