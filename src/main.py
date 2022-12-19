import adaptive_huffman
import utils
import string

bytes = utils.read_from_file("src/test1.txt")
alphabet = list(string.ascii_lowercase)
coder = adaptive_huffman.AdaptiveHuffmanEncoderDecoder(len(alphabet), alphabet)
coder.encode(bytes)
# print("JIIIIIIIIIIIIIIIIP")
