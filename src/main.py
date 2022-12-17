import adaptive_huffman
import utils

bytes = utils.read_from_file("test1.txt")
coder = adaptive_huffman.AdaptiveHuffmanEncoderDecoder(bytes, 0)
coder.encode()
print("JIIIIIIIIIIIIIIIIP")