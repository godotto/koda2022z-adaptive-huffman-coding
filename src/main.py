import utils
from os import getcwd

print(getcwd())

IMAGE_FILES_DIR = "../test_data/images/"
DISTRIBUTION_FILES_DIR = "../test_data/distributions/"
TEST_RESULTS_DIR = "../test_results/"

input_file = IMAGE_FILES_DIR + "barbara.pgm"  # file to be encoded
encoded_filename = TEST_RESULTS_DIR + "test_adaptive.bin"
decoded_filename = TEST_RESULTS_DIR + "adaptive_decoded.pgm"

encoded_file_static = TEST_RESULTS_DIR + "test_static.bin"
decoded_filename_static = TEST_RESULTS_DIR + "static_decoded.pgm"

histogram_filename = TEST_RESULTS_DIR + "histogram.png"

utils.adaptive_huff(input_file, encoded_filename, decoded_filename, histogram_filename)
utils.static_huff(input_file, encoded_file_static, decoded_filename_static)

