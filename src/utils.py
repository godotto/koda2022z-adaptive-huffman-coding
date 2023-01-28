import string

from dahuffman import HuffmanCodec
from bitstring import BitArray

import adaptive_huffman
from node import Node
import test_utils

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


def write_to_file(byte_array: bytearray, filename: str):
    with open(filename, "wb") as binary_file:
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


def read_pgm_file(file_to_encode: str):

    pgmf = read_from_file(file_to_encode)
    pgmf_base = pgmf[:70]
    hash_index = pgmf_base.find(b'#')
    if hash_index != -1:
        newlines = 4
    else:
        newlines = 3

    m = 0
    actual_nl_index = 0
    while m < newlines:
        actual_nl_index = pgmf.find(b'\n', actual_nl_index + 1)
        m = m + 1

    pgmf_headline = pgmf[:actual_nl_index + 1]
    pgmf = pgmf[actual_nl_index + 1:]
    input_bytes = pgmf
    alphabet = list(range(0, 256))

    return input_bytes, alphabet, pgmf_headline


def read_txt_file(file_to_encode: str):
    input_filename = file_to_encode
    input_bytes = read_from_file(input_filename)
    alphabet = string.ascii_lowercase
    alphabet = [ord(a) for a in alphabet]

    return input_bytes, alphabet


def encode(input_bytes: bytearray, alphabet, encoded_file: str):
    coder = adaptive_huffman.AdaptiveHuffmanEncoderDecoder(alphabet)
    code = coder.encode(input_bytes, encoded_file)
    return code, coder


# decoding
def decode(alphabet, encoded_file: str):
    decoder = adaptive_huffman.AdaptiveHuffmanEncoderDecoder(alphabet)
    decoded = decoder.decode(encoded_file)
    return decoded


def write_decoded_to_pgm(pgmf_headline: bytes, decoded: bytearray, decoded_file: str):
    with open(decoded_file, "wb") as bin_file:
        bin_file.write(bytearray(pgmf_headline))
        bin_file.close()

    with open(decoded_file, "ab") as bin_file:
        bin_file.write(decoded)
        bin_file.close()


def write_decoded_to_txt(decoded: bytearray, decoded_file: str):
    write_to_file(decoded, decoded_file)


def adaptive_huff(input_filename: str, encoded_file: str, decoded_filename: str, pgm: bool = True):
    if pgm == True:
        input_bytes, alphabet, pgmf_prefix = read_pgm_file(input_filename)

        print("####### HISTOGRAM AND ENTROPY GENERATION START #######")
        test_utils.generate_histogram(input_bytes, "histogram.png")
        print(f"Input data entropy: {test_utils.input_data_entropy(input_bytes)}")
        print("####### HISTOGRAM AND ENTROPY GENERATION END #######\n")

        print("####### ADAPTIVE ENCODING START #######")
        code, coder = encode(input_bytes, alphabet, encoded_file)
        print(f"Average bit lenght: {test_utils.average_bit_lenght(coder, input_bytes, code)}")
        print("####### ADAPTIVE ENCODING END #######\n")
        print("####### ADAPTIVE DECODING START #######")
        decoded = decode(alphabet, encoded_file)
        print("####### ADAPTIVE DECODING END #######\n")
        write_decoded_to_pgm(pgmf_prefix, decoded, decoded_filename)
    else:
        input_bytes, alphabet = read_txt_file(input_filename)
        encode(input_bytes, alphabet, encoded_file)
        decoded = decode(alphabet, encoded_file)
        write_decoded_to_txt(decoded, decoded_filename)


def static_huff(input_filename: str, encoded_file: str, decoded_filename: str, if_pgm: bool = True):
    if if_pgm == True:
        input_bytes, _, pgmf_prefix = read_pgm_file(input_filename)
        print("####### STATIC ENCODING START #######")
        codec = HuffmanCodec.from_data(input_bytes)
        static_code = codec.encode(input_bytes)
        print(f"Number of bytes of sequence encoded with static Huffman coder: {len(static_code) * 8}")
        print(f"Average bit lenght: {test_utils.average_bit_lenght(codec, input_bytes, static_code)}")
        print("####### STATIC ENCODING END #######\n")
        write_to_file(static_code, encoded_file)
        print("####### STATIC DECODING START #######")
        decoded_static = codec.decode(static_code)
        print("####### STATIC DECODING END #######\n")
        write_decoded_to_pgm(pgmf_prefix, decoded_static, decoded_filename)
    else:
        input_bytes, _ = read_txt_file(input_filename)
        codec = HuffmanCodec.from_data(input_bytes)
        static_code = codec.encode(input_bytes)
        write_to_file(static_code, encoded_file)
        decoded_static = codec.decode(static_code)
        write_decoded_to_txt(decoded_static, decoded_filename)