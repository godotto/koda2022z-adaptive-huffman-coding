import node
import utils
import string


NYT = "NYT"


class AdaptiveHuffmanEncoderDecoder:
    def __init__(self, alphabet_size: int, alphabet):
        self.alphabet_size = alphabet_size

        self.e = alphabet_size.bit_length() - 1
        self.r = alphabet_size - 2 ** self.e

        self.root = node.Node(0, NYT, alphabet_size * 2 - 1)

        self.nodes_list = [self.root]
        print("e: " + str(self.e))
        print("r: " + str(self.r))

        # used alphabet
        self.alphabet = alphabet

        # generating fixed code for used alphabet
        self.fixed_code = []
        for i, _ in enumerate(self.alphabet):
            if 0 <= i <= 2 * self.r - 1:
                bin_a = '{0:b}'.format(i)
                bin_a = bin_a.zfill(self.e + 1)
            else:
                bin_a = '{0:b}'.format(i - self.r)
                bin_a = bin_a.zfill(self.e)
            self.fixed_code.append(bin_a)

    def encode(self, input_data: bytearray):
        code = ""
        for byte in input_data:
            symbol_code = utils.print_code_new(
                self.root, byte, self.fixed_code, self.alphabet)
            print(chr(byte))
            print(symbol_code + " ")
            code += symbol_code
            utils.update(self.root, byte, self.nodes_list)
        print(code)
        utils.add_padding(code)
        byte_array = utils.convert_to_bytes(code)
        utils.write_to_file(byte_array)
