import adaptive_huffman
import utils
import string

bytes = utils.read_from_file("test1.txt")
alphabet = list(string.ascii_lowercase)
coder = adaptive_huffman.AdaptiveHuffmanEncoderDecoder(26, alphabet)
coder.encode(bytes)
print("JIIIIIIIIIIIIIIIIP")
