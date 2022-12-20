import adaptive_huffman
import utils
import string

##encoding
bytes = utils.read_from_file("test1.txt")
alphabet = string.ascii_lowercase
alphabet = [ord(a) for a in alphabet]
coder = adaptive_huffman.AdaptiveHuffmanEncoderDecoder(len(alphabet), alphabet)
code = coder.encode(bytes)

##decoding
# decoder = adaptive_huffman.AdaptiveHuffmanEncoderDecoder(len(alphabet), alphabet)
# binary_file = "my_binary_file.bin"
# decoder.decode(binary_file) #?

