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
        pass

    def encode(self, input_data: bytearray):
        code = ""
        for byte in input_data:
            symbol_code = utils.print_code(
                self.root, byte, self.fixed_code, self.alphabet)
            code += symbol_code
            utils.update(self.root, byte, self.nodes_list)
        print('Endcoded sequence - write to binary file')
        #print(code)
        byte_array = utils.convert_to_bytes(code)
        utils.write_to_file(byte_array)
        print(f'Count of bytes of original sequence {len(input_data)}')
        print(f'Count of bytes of encoded sequence {len(byte_array)}')
        return code

    def decode(self, filename: str):
        input = utils.read_from_binary_file(filename)
        print('Encoded sequence - read form a binary file')
        #print(input)
        i = -1  # current bit from the string
        bits = ""  # current bits input
        decoded = bytearray()
        #decoded = ""  # decoded sequence
        current_node = self.root  # begin with root
        while True:
            if current_node.symbol:
                if current_node.symbol == NYT:
                    bits = ""
                    i += 1
                    bits += input[i:i+self.e]
                    i += self.e - 1
                    if int(bits, 2) < self.r:
                        i += 1
                        bits += input[i]
                    else:
                        bits = format(int(bits, 2) + self.r, 'b')
                    letter = self.alphabet[int(bits, 2)]
                else:
                    letter = current_node.symbol

                #decoded += str(letter)
                decoded.append(letter)

                utils.update(self.root, letter, self.nodes_list)
                current_node = self.root

                bits = ""

                if i == len(input) - 1:
                    break
            else:
                i += 1
                bit = input[i]
                current_node = current_node.right if int(
                    bit) else current_node.left
                bits += bit
        #utils.write_to_file(decoded)
        #print(decoded)

        return decoded