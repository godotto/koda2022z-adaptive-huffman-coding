import adaptive_huffman
import utils
import string

##encoding
bytes = utils.read_from_file("test1.txt")
alphabet = list(string.ascii_lowercase)
coder = adaptive_huffman.AdaptiveHuffmanEncoderDecoder(len(alphabet), alphabet)
code = coder.encode(bytes)

#decoding
binary_file = "my_binary_file.bin"
coder.decode(binary_file) #?

