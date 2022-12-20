import numpy
from bitstring import BitArray
from node import Node

NYT = "NYT"
LEFT_CODE = '0'
RIGHT_CODE = '1'


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


def print_code(root: Node, symbol, fixed_code, alphabet):
    searched_node = find_node_symbol(root, symbol)
    code_of_symbol = ""
    if searched_node:
        while searched_node.parent:
            if searched_node == searched_node.parent.left:
                code_of_symbol += LEFT_CODE
            else:
                code_of_symbol += RIGHT_CODE
            searched_node = searched_node.parent
        code_of_symbol = code_of_symbol[slice(None, None, -1)]

        return (code_of_symbol)
    else:
        code_of_symbol = print_code(root, NYT, fixed_code, alphabet)
        #symbol_chr = chr(symbol)
        index = alphabet.index(symbol)
        code_for_new_symbol = code_of_symbol + fixed_code[index]
        return (code_for_new_symbol)


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


def convert_to_bytes(code: str):

    padding_len = 8 - len(code) % 8
    pad_l_b = '{0:b}'.format(padding_len)
    pad_l_b = pad_l_b.zfill(8)
    code = pad_l_b + code.ljust(padding_len + len(code), '0')
    byte_array = bytearray()
    for i in range(0, len(code), 8):
        byte = code[i:i + 8]
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

def read_from_binary_file(filename: str):
    with open(filename, mode="rb") as txt_file:
        contents = txt_file.read()
    a = BitArray(bytes=contents)
    raw_bin_string = a.bin
    how_many_pads = int(raw_bin_string[0:8], 2)
    original_code = raw_bin_string[8:-how_many_pads]
    return original_code

def update(root: Node, symbol, nodes_list):
    current_node = find_node_symbol(root, symbol)

    if current_node is None:  # it means the first appearnace
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
