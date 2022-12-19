import numpy

from node import Node

NYT = "NYT"


def switch_nodes(left_node: Node, right_node: Node):
    # switch references to the left node
    left_node.left, right_node.left = right_node.left, left_node.left

    # switch references to the right node
    left_node.right, right_node.right = right_node.right, left_node.right

    # switch contained symbols
    left_node.symbol, right_node.symbol = right_node.symbol, left_node.symbol

    # update info about parents
    if left_node.left is not None:
        left_node.left.parent = left_node

    if left_node.right is not None:
        left_node.right.parent = left_node

    if right_node.left is not None:
        right_node.left.parent = right_node

    if right_node.right is not None:
        right_node.right.parent = right_node


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


def update(root: Node, symbol, nodes_list):
    current_node = find_node_symbol(root, symbol)

    if current_node is None: # it means the first appearnace
        current_node = find_node_symbol(root, NYT)

        new_nyt = Node(0, NYT, current_node.number - 2, current_node)
        new_external = Node(1, symbol, current_node.number - 1, current_node)
        
        nodes_list.append(new_nyt)
        nodes_list.append(new_external)

        current_node.left = new_nyt
        current_node.right = new_external
        current_node.symbol = None
        current_node.weight += 1
    else:
        for node in nodes_list:
            if node.weight == current_node.weight and node != current_node.parent and node.number > current_node.number:
                switch_nodes(node, current_node)
                node.weight += 1
                current_node = node
                break
        else:
            current_node.weight += 1

    while current_node.parent != None:
        current_node = current_node.parent

        for node in nodes_list:
            if node.weight == current_node.weight and node != current_node.parent and node.number > current_node.number:
                switch_nodes(node, current_node)
                node.weight += 1
                current_node = node
                break
        else:
            current_node.weight += 1
