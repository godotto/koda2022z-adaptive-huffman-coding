

import adaptive_huffman
import utils
import string

input_file = "geometr_05.pgm" #file to be encoded
encoded_filename = "test_adaptive.bin"
decoded_filename = "adaptive_decoded.pgm"

encoded_file_static = "test_static.bin"
decoded_filename_static = "static_decoded.pgm"

# encoding
utils.adaptive_huff(input_file, encoded_filename, decoded_filename)
utils.static_huff(input_file, encoded_file_static, decoded_filename_static)
