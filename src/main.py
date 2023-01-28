import adaptive_huffman
import utils
import string

input_file = "src/geometr_05.pgm" #file to be encoded
encoded_filename = "src/test_adaptive.bin"
decoded_filename = "src/adaptive_decoded.pgm"

encoded_file_static = "src/test_static.bin"
decoded_filename_static = "src/static_decoded.pgm"

histogram_filename = "histogram.png"

pgm = True

# encoding
utils.adaptive_huff(input_file, encoded_filename, decoded_filename, pgm)
utils.static_huff(input_file, encoded_file_static, decoded_filename_static, pgm)
