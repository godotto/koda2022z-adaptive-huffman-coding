import node
import utils


NYT = "NYT"


class AdaptiveHuffmanEncoderDecoder:
    def __init__(self, input_data: bytearray, alphabet_size: int):
        self.input_data = input_data
        self.alphabet_size = alphabet_size

        self.e = alphabet_size.bit_length() - 1
        self.r = alphabet_size - 2 ** self.e

        self.root = node.Node(0, NYT)

    def encode(self):
        code = ""
        for i in range(len(self.input_data)):
            symbol_code, first_appearance = utils.print_code(self.root, self.input_data[i])
            print(symbol_code + " ")
            code += symbol_code
            utils.update(self.root, self.input_data[i], first_appearance)
        utils.add_padding(code)
        byte_array = utils.convert_to_bytes(code)
        utils.write_to_file(byte_array)


