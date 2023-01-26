import adaptive_huffman
import utils
import string

input_filename = "test.txt"
output_filename = "test.bin"

# 6 lines below - uncomment when pgm file is to by coded
pgmf = utils.read_from_file("geometr_05.pgm")
last_index = pgmf.rfind(b'\n')
pgmf_prefix = pgmf[:last_index+1]
pgmf = pgmf[last_index+1:]
input_bytes = pgmf
alphabet = list(range(0, 255))

# 3 lines below - uncomment when txt file is to be coded
# input_bytes = utils.read_from_file(input_filename)
# alphabet = string.ascii_lowercase
# alphabet = [ord(a) for a in alphabet]

# encoding

coder = adaptive_huffman.AdaptiveHuffmanEncoderDecoder(len(alphabet), alphabet)
code = coder.encode(input_bytes, output_filename)

# decoding
decoder = adaptive_huffman.AdaptiveHuffmanEncoderDecoder(len(alphabet), alphabet)
input_filename = "test.bin"
output_filename = "test_decoded.txt"
decoded = decoder.decode(input_filename, output_filename)

 ##saving decoded byte sequence to a pmg file
with open("decoded_binary_file.pgm", "wb") as bin_file:
    # Write bytes to file
    bin_file.write(bytearray(pgmf_prefix))
    bin_file.close()

with open("decoded_binary_file.pgm", "ab") as bin_file:
    # Write bytes to file
    bin_file.write(decoded)
    bin_file.close()