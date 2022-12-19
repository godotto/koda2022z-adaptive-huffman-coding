import adaptive_huffman
import utils

bytes = utils.read_from_file("src/test1.txt")
coder = adaptive_huffman.AdaptiveHuffmanEncoderDecoder(26)
coder.encode(bytes)
print("JIIIIIIIIIIIIIIIIP")
