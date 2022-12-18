import numpy

from node import Node

NYT = "NYT"


def switch_nodes(left_node: Node, right_node: Node):
    # switch references to the left node
    left_node.left, right_node.left = right_node.left, left_node.left

    # switch references to the right node
    left_node.right, right_node.right = right_node.right, left_node.right

    # switch references to the parent node (if needed)
    left_node.parent, right_node.parent = right_node.parent, left_node.parent

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
            code_for_new_symbol = current_node.code + '1'
            return (code_for_new_symbol, True)
        if current_node.left:
            current_node.left.code = current_node.code + '0'
            nodes_to_check.append(current_node.left)
        if current_node.right:
            current_node.right.code = current_node.code + '1'
            nodes_to_check.append(current_node.right)

    # returns code for a new symbok and true if it is a new symbol on a tree
    return (current_node.code, True)


def update(root: Node, symbol, first_apperance):
    current_node: Node = None
    counter = 0
    while True:
        if first_apperance:
            current_node = find_node_symbol(root, NYT)

            # Add new symbol to the right of current node
            current_node.right = Node(1, symbol)
            current_node.right.parent = current_node

            # Set let node to NYT
            current_node.left = Node(0, NYT)
            current_node.left.parent = current_node

            # Update current node
            current_node.weight += 1
            current_node.symbol = ""
        else:
            if not current_node:
                current_node = find_node_symbol(root, symbol)
            # find node that has the same weight and is not current node or its child
            node_to_replace = find_node_to_swap(root, current_node)
            if node_to_replace is not current_node.parent:
                switch_nodes(current_node, node_to_replace)
                current_node = node_to_replace

            current_node.weight += 1

        if not current_node.parent:
            break
        current_node = current_node.parent
        first_apperance = False
        counter += 1
        # print(str(counter) + " ")


def find_node_symbol(root: Node, symbol) -> Node:
    if root.symbol == symbol:
        return root

    if root.left:
        node = find_node_symbol(root.left, symbol)
        if node:
            return node

    if root.right:
        node = find_node_symbol(root.right, symbol)
        if node:
            return node

    return None


def find_node_to_swap(root: Node, node_to_swap: Node) -> Node:
    if root.weight == node_to_swap.weight:
        if root is node_to_swap or root.parent is node_to_swap:
            return None
        else:
            return root

    if root.left:
        node = find_node_to_swap(root.left, node_to_swap)
        if node:
            return node

    if root.right:
        node = find_node_to_swap(root.right, node_to_swap)
        if node:
            return node

    return None


def add_padding(code: str):
    padding_len = 8 - len(code) % 8
    zeros = numpy.zeros(padding_len, dtype=int)
    zero_s = numpy.array2string(zeros)
    code += zero_s
    code = str(padding_len) + code


def convert_to_bytes(code: str):
    byte_array = bytearray()
    for i in range(0, len(code), 8):
        byte = code[1:1 + 8]
        byte_array.append(int(byte, 2))
    return byte_array


def write_to_file(byte_array: bytearray):
    with open("my_binary_file.bin", "wb") as binary_file:
        # Write bytes to file
        binary_file.write(byte_array)


def read_from_file(filename: str):
    with open(filename, "rb") as binary_file:
        byte_array = binary_file.read()
    return byte_array
