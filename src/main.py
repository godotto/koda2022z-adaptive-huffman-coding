import adaptive_huffman
import utils
import string

# encoding
input_filename = "test.txt"
output_filename = "test.bin"
input_bytes = utils.read_from_file(input_filename)
alphabet = string.ascii_lowercase
alphabet = [ord(a) for a in alphabet]
coder = adaptive_huffman.AdaptiveHuffmanEncoderDecoder(len(alphabet), alphabet)
code = coder.encode(input_bytes, output_filename)

# decoding
decoder = adaptive_huffman.AdaptiveHuffmanEncoderDecoder(len(alphabet), alphabet)
input_filename = "test.bin"
output_filename = "test_decoded.txt"
decoder.decode(input_filename, output_filename)
