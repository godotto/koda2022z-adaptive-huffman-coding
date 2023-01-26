from importlib.resources import contents
from pgm_reader import Reader

import matplotlib.pyplot as plt
import utils
from bitstring import BitArray

pgmf = utils.read_from_file("barbara.pgm")
print(pgmf[:50])
#pgmf_b = utils.write_to_file(pgmf)
#pgmf = 'barbara.pgm'
# reader = Reader()
# image = reader.read_pgm(pgmf)
# width = reader.width
# print(width)
# with open('barbara.pgm', 'rb') as f:
#     s = f.read()
last_index = pgmf.rfind(b'\n')
print(last_index)
print(pgmf.count(b'\n'))

pgmf = pgmf[last_index+1:]
print(pgmf[:50])