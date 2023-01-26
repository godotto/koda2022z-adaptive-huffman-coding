import adaptive_huffman
import utils
import string


##file preparing

## 6 lines below - uncomment when pgm file is to by coded
pgmf = utils.read_from_file("barbara.pgm")
last_index = pgmf.rfind(b'\n')
pgmf_prefix = pgmf[:last_index+1]
pgmf = pgmf[last_index+1:]
bytes = pgmf
alphabet = list(range(0, 255))

## 3 lines below - uncomment when txt file is to be coded
# bytes = utils.read_from_file("test1.txt")
# alphabet = list(string.ascii_lowercase)
# alphabet = [ord(a) for a in alphabet]

 ##encoding
coder = adaptive_huffman.AdaptiveHuffmanEncoderDecoder(len(alphabet), alphabet)
code = coder.encode(bytes)

 ##decoding
decoder = adaptive_huffman.AdaptiveHuffmanEncoderDecoder(len(alphabet), alphabet)
binary_file = "my_binary_file.bin"
decoded = decoder.decode(binary_file) #?

 ##saving decoded byte sequence to a pmg file
with open("decoded_binary_file.pgm", "wb") as bin_file:
    # Write bytes to file
    bin_file.write(bytearray(pgmf_prefix))
    bin_file.close()

with open("decoded_binary_file.pgm", "ab") as bin_file:
    # Write bytes to file
    bin_file.write(decoded)
    bin_file.close()



