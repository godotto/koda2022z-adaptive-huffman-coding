import node

NYT = "NYT"


class AdaptiveHuffmanEncoderDecoder:
    def __init__(self, input_data: bytes, alphabet_size: int):
        self.input_data = input_data
        self.alphabet_size = alphabet_size

        self.e = alphabet_size.bit_length() - 1
        self.r = alphabet_size - 2 ** self.e

        self.root = node.Node(0, NYT)
